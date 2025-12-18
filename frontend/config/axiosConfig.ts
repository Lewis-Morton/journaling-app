import axios from 'axios';
import SecureStore from 'expo-secure-store';

const API_BASE_URL = '192.168.56.1:8000/api/';

const api = axios.create({
    baseURL: API_BASE_URL,
    headers: {
        'Content-Type': 'application/json',
    },
});
// request interceptor to add token to each request
api.interceptors.request.use(
    async (config) => {
        const token = await SecureStore.getItemAsync('accessToken');
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);

// respose interceptor to handle token refresh
api.interceptors.response.use(
    (response) => response,
    async (error) => {
        const originalRequest = error.config;

        if (error.response?.status === 401 && !originalRequest._retry) {
            originalRequest._retry = true;

            try {
                const refreshToken = await SecureStore.getItemAsync('refreshToken');

                if (refreshToken) {
                    const response = await axios.post(
                        `${API_BASE_URL}token/refresh/`,
                        { refresh: refreshToken }
                    );

                    const { access } = response.data;
                    await SecureStore.setItemAsync('accesstToken', access);

                    originalRequest.headers.Authorization = `Bearer ${access}`;
                    return api(originalRequest);
                }
            } catch (refreshError) {

                await SecureStore.deleteItemAsync('accessToken');
                await SecureStore.deleteItemAsync('refreshToken');
                return Promise.reject(refreshError);
            }
        }
            
        return Promise.reject(error);    

    }
);

export default api