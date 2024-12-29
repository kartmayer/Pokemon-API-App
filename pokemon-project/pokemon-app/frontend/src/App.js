import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Login from './components/Login';
import Pokedex from './components/Pokedex';
import Pokemon from './components/Pokemon';

function App() {
  return (
    <Router>
      <div>
        <Switch>
          <Route path="/" exact component={Login} />
          <Route path="/pokedex" component={Pokedex} />
          <Route path="/pokemon/:id" component={Pokemon} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;