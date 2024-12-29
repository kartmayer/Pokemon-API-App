import React from 'react';

const Pokemon = ({ pokemon }) => {
    return (
        <div className="pokemon-card">
            <h2>{pokemon.name}</h2>
            <img src={pokemon.sprites.front_default} alt={pokemon.name} />
            <p>Height: {pokemon.height}</p>
            <p>Weight: {pokemon.weight}</p>
            <h3>Types:</h3>
            <ul>
                {pokemon.types.map((typeInfo) => (
                    <li key={typeInfo.type.name}>{typeInfo.type.name}</li>
                ))}
            </ul>
        </div>
    );
};

export default Pokemon;