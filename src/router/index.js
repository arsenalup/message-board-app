import Vue from 'vue'
import Router from 'vue-router'
import Home from '../views/Home.vue'
import About from '../views/About.vue'
import Contact from '../views/Contact.vue'
import Message from '../views/Message.vue'

Vue.use(Router)

//配置路径与组建的对应关系
const routes = [
    {
        path: '/',
        component: Home
    },
    {
        path: '/about',
        component: About
    },
    {
        path: '/contact',
        component: Contact
    },
    {
        path: '/Message',
        component: Message
    },
]

export default new Router({
    mode: 'history',
    routes: routes
})