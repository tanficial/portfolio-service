import axios from "axios";

const apiPath = process.env.REACT_APP_BACKEND_URL + "/portfolio";

export const fetchPortfolio = async (userId) => {
    const response = await axios.get(`${apiPath}/${userId}`);
    return response.data.portfolio;
}