import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import AcroVue from '@arco-design/web-vue'

import App from '@/App.vue'
import router from '@/router'

import '@arco-design/web-vue/dist/arco.css'
import '@/assets/styles/main.css'

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(AcroVue)

app.mount('#app')
