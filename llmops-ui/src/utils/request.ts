// 1. 接口超时， 100s
// 2. 不需要写api前缀，比如http://localhost:500 
// 3. 我们经常使用get和post， 所以需要封装两个函数
// 4. 每次获取数据都要使用response.json()才可以获取数据，需要封装

import { Message } from '@arco-design/web-vue'
import { apiPrefix, httpCode } from '@/config';

const TIMEOUT = 100000;

console.log(apiPrefix);

// 2.基础的配置
const baseFetchOptions = {
    method: 'GET',
    mode: 'cors',
    credentials: 'include',
    headers: new Headers({
        'Content-Type': 'application/json',
    }),
    redirect: 'follow',
};

// fetch参数类型
type FetchOptionType = Omit<RequestInit, 'body'> & {
    params?: Record<string, string>
    body?: BodyInit | Record<string, any> | null
};

// 2. 封装基础的fetech请求
const baseFetch = <T>(url: string, fetchOptions: FetchOptionType) => {
    // 将所有的配置信息合并起来
    const options: typeof baseFetchOptions & FetchOptionType = Object.assign(
        {}, baseFetchOptions, fetchOptions)

    //组装url
    let urlWithPrefix = `${apiPrefix}${url.startsWith('/') ? '' : '/'}${url}`

    // 7.解构出对应的请求方法、params、body参数
    const { method, params, body } = options

    // 8.如果请求是GET方法，并且传递了params参数
    if (method === 'GET' && params) {
        const paramsArray: string[] = []
        Object.keys(params).forEach((key) => {
            paramsArray.push(`${key}=${encodeURIComponent(params[key])}`)
        })
        if (urlWithPrefix.search(/\?/) === -1) {
            urlWithPrefix += `?${paramsArray.join('&')}`
        } else {
            urlWithPrefix += `&${paramsArray.join('&')}`
        }

        delete options.params
    }



    // 9.处理post传递的数据
    if (body) {
        options.body = JSON.stringify(body)
    }

    // 10.同时发起两个Promise(或者是说两个操作，看谁先返回，就先结束)
    return Promise.race([
        // 11.使用定时器来检测是否超时
        new Promise((resolve, reject) => {
            setTimeout(() => {
                reject('接口已超时')
            }, TIMEOUT)
        }),
        // 12.发起一个正常请求
        new Promise((resolve, reject) => {
            globalThis
                .fetch(urlWithPrefix, options as RequestInit)
                .then(async (res) => {
                    const json = await res.json()
                    if (json.code === httpCode.success) {
                        resolve(json)
                    } else {
                        Message.error(json.message)
                        reject(new Error(json.message))
                    }
                })
                .catch((err) => {
                    Message.error(err.message)
                    reject(err)
                })
        }),
    ]) as Promise<T>
}

export const request = <T>(url: string, options = {}) => {
    return baseFetch<T>(url, options)
}

export const get = <T>(url: string, options = {}) => {
    return request<T>(url, Object.assign({}, options, { method: 'GET' }))
}

export const post = <T>(url: string, options = {}) => {
    return request<T>(url, Object.assign({}, options, { method: 'POST' }))
}
