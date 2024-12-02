import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import Specializations from './components/specializations/Specializations';
import Services from './components/services/Services';
import Profile from './components/profile/Profile';
import GoogleAuthCallback from './components/profile/loginAndRegister/items/GoogleAuthCallback';
import Order from './components/order/Order';
import Admin from './components/admin/Admin';
import DoctorInfo from './components/admin/doctors/items/DoctorInfo';
import EditDoctor from './components/admin/doctors/items/EditDoctor';
import CreateDoctor from './components/admin/doctors/items/CreateDoctor';
import News from './components/news/News';

const router = createBrowserRouter([
  {
    path: "",
    element: <App />,
  },
  {
    path: "/specializations",
    element: <Specializations />,
  },
  {
    path: "/services/:id",
    element: <Services />,
  },
  {
    path: "/profile",
    element: <Profile />,
  },
  {
    path: "/oauth",
    element: <GoogleAuthCallback/>,
  },
  {
    path: "/order/:id",
    element: <Order/>,
  },
  {
    path: "/admin",
    element: <Admin/>,
  },
  {
    path: "/admin/doctor/:id",
    element: <DoctorInfo/>
  },
  {
    path: "/admin/doctor/update/:id",
    element: <EditDoctor/>
  },
  {
    path: "/admin/doctor/create",
    element: <CreateDoctor/>
  },
  {
    path: "/news",
    element: <News/>
  }
]);

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);

reportWebVitals();
