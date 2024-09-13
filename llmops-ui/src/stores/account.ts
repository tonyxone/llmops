import { defineStore } from 'pinia'
import { ref } from 'vue'

//初始值
const initAccount = {
  name: 'test',
  email: 'test@163.com',
  avatar: '',
}

export const useAccountStore = defineStore('account', () => {
  // 1. 定义数据
  const account = ref({ ...initAccount })
  // 2.函数
  function update(params: any) {
    Object.assign(account.value, params)
  }

  function clear() {
    account.value = { ...initAccount }
  }
  return { account, update, clear }
})
