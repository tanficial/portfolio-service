import axios from "axios";

const apiPath = process.env.REACT_APP_BACKEND_URL + "/auth";

export const loginRequest = async (email, password) => {
    const response = await axios.post(`${apiPath}/login`, { email, password });
    const userId = response.data.user.id;
    window.sessionStorage.setItem("id", userId);
    return userId;
};

export const logoutRequest = async () => {
    await axios.get(`${apiPath}/logout`);
    window.sessionStorage.clear();
};

export const registerRequest = async (email, password, name) => {
    await axios.post(`${apiPath}/register`, { email, password, name });
}