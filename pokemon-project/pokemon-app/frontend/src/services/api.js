import axios from 'axios';

const API_URL = 'http://localhost:8000/api'; // Adjust the URL as needed

// Function to log in a user
export const loginUser = async (credentials) => {
    try {
        const response = await axios.post(`${API_URL}/users/login/`, credentials);
        return response.data;
    } catch (error) {
        throw error.response.data;
    }
};

// Function to fetch Pokémon data
export const fetchPokemon = async (pokemonName) => {
    try {
        const response = await axios.get(`https://pokeapi.co/api/v2/pokemon/${pokemonName}`);
        return response.data;
    } catch (error) {
        throw error;
    }
};

// Function to add Pokémon to the user's Pokédex
export const addPokemonToPokedex = async (userId, pokemonData) => {
    try {
        const response = await axios.post(`${API_URL}/pokedex/${userId}/add/`, pokemonData);
        return response.data;
    } catch (error) {
        throw error.response.data;
    }
};

// Function to get the user's Pokédex
export const getUserPokedex = async (userId) => {
    try {
        const response = await axios.get(`${API_URL}/pokedex/${userId}/`);
        return response.data;
    } catch (error) {
        throw error.response.data;
    }
};