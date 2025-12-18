import SecureStore from 'expo-secure-store';
import api from '../config/axiosConfig';

interface LoginCredentials {
    username: string;
    password: string;
}

interface RegisterData {
    usernames: string;
    email: string;
    password: string;
    password2: string;
}

interface TokenResponse {
    access: string;
    refresh: string;
}

export const authService = {
    login: async (credentials: LoginCredentials): Promise<TokenResponse> => {
        const response = await api.post<TokenResponse>('token/', credentials);
        const { access, refresh } = response.data;

        await SecureStore.setItemAsync('accessToken', access);
        await SecureStore.setItemAsync('refreshTOken', refresh);

        return response.data;
    },

    register: async (userData: RegisterData) => {
        const response = await api.post('users/register/', userData);
        return response.data;
    },

    logout: async () => {
        await SecureStore.deleteItemAsync('accessToken');
        await SecureStore.deleteItemAsync('refreshToken');
    },

    isAuthenticated: async (): Promise<boolean> => {
        const token = await SecureStore.getItemAsync('accessToken');
        return !!token;
    },

    getCurrentUser: async () => {
        const response = await api.get('users/me/');
        return response.data;
    },
};