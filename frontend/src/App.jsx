import React, { useState } from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';

import 'styles/reset.css'
import 'styles/global.css'

import Header from 'components/Header';

import Login from 'pages/Login';
import Register from 'pages/Register';
import Portfolio from 'pages/Portfolio';
import Search from 'pages/Search';
import NotFoundPage from 'pages/NotFoundPage';

function App() {
  const [loginId, setLoginId] = useState(window.sessionStorage.getItem("id"));

  return (
    <div className="App">
      <BrowserRouter>
        <Header loginId={loginId} setLoginId={setLoginId} />
        <Switch>
          <Route axact path="/login">
            <Login setLoginId={setLoginId} />
          </Route>

          <Route exact path="/register">
            <Register />
          </Route>

          <Route exact path="/search">
            <Search loginId={loginId} setLoginId={setLoginId} />
          </Route>

          <Route exact path="/page404">
            <NotFoundPage loginId={loginId} />
          </Route>

          <Route path="/:id">
            <Portfolio loginId={loginId} setLoginId={setLoginId} />
          </Route>

          <Route exact path="/">
            <Portfolio loginId={loginId} setLoginId={setLoginId} />
          </Route>
        </Switch>
      </BrowserRouter>
    </div>
  );
}

export default App;
