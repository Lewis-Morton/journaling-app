import api from '../config/axiosConfig';

interface JournalEntry {
    id?: number;
    text: string;
    mood: string;
    created_at?: string;
    updated_at?: string;
}

export const journalService = {
    getJournals: async (): Promise<JournalEntry[]> => {
        const response = await api.get<JournalEntry[]>('journals/');
        return response.data;
    },

    getJournal: async (id: number): Promise<JournalEntry> => {
        const response = await api.get<JournalEntry>('journals/${id}/');
        return response.data
    },

    createJournal: async (journalData: Omit<JournalEntry, 'id' | 'created_at' | 'updated_at'>): Promise<JournalEntry> => {
        const response = await api.post<JournalEntry>('journals/create/', journalData);
        return response.data;
    },

    updateJournal: async (id: number, journalData: Partial<JournalEntry>): Promise<JournalEntry> => {
        const response = await api.put<JournalEntry>(`journals/${id}/update/`, journalData);
        return response.data;
    },

    deleteJournal: async (id: number): Promise<void> => {
        await api.delete(`journals/${id}/delete/`);
    },
};