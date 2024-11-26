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
  }
]);

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);

reportWebVitals();
