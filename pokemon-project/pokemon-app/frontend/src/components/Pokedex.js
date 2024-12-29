import React, { useEffect, useState } from 'react';
import { fetchUserPokedex } from '../services/api';
import Pokemon from './Pokemon';

const Pokedex = () => {
    const [pokedex, setPokedex] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const getPokedex = async () => {
            const data = await fetchUserPokedex();
            setPokedex(data);
            setLoading(false);
        };

        getPokedex();
    }, []);

    if (loading) {
        return <div>Loading...</div>;
    }

    return (
        <div>
            <h1>Your Pokedex</h1>
            <div className="pokedex-container">
                {pokedex.map(pokemon => (
                    <Pokemon key={pokemon.id} pokemon={pokemon} />
                ))}
            </div>
        </div>
    );
};

export default Pokedex;