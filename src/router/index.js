import Vue from 'vue'
import Router from 'vue-router'

import Main from '../views/Main'
import Login from '../views/Login'
import UserProfile from '../views/user/Profile'
import UserList from '../views/user/List'
Vue.use(Router);

export default new Router({
  router:[
  {
    path: '/main',
    component:Main,
    children:[
        {path: '/user/Profile',component:UserProfile},
        {path: '/user/List',component:UserList}]
  },
  {
    path: '/login',
    component:Login
  }
  ]
});
