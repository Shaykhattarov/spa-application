import { Navigate, Outlet } from "react-router-dom";



function PrivateRoute() {
    const hasToken = true;

    return (
        hasToken ? <Outlet /> : <Navigate to="/registration" />
    );
}


export default PrivateRoute;