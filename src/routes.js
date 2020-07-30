import LandingPage from './components/LandingPage.vue'
import RegisterPage from './components/RegisterPage/RegisterPage.vue'
import LoginPage from './components/LoginPage/LoginPage.vue'
import FaceVerificationPage from './components/FaceVerification/FaceVerification.vue'
import ExamPage from './components/ExamPage/ExamPage.vue'

export default [
    {path: '/', component: LandingPage},
    {path: '/register', component: RegisterPage},
    {path: '/login', component: LoginPage},
    {path: '/faceverification', component: FaceVerificationPage},
    {path: '/exam', component: ExamPage}
]