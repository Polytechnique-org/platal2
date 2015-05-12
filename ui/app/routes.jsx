'use strict';

// Global imports
var React = require('react');
var Router = require('react-router');

// Add to JSX scope
var Route = Router.Route;
var DefaultRoute = Router.DefaultRoute;

// Views
var MainView = require('./views/main.jsx');
var HomeView = require('./views/home.jsx');
var InfoView = require('./views/info.jsx');

var routes = (
    <Route name="app" path="/" handler={MainView}>
      <Route name="info" handler={InfoView}/>
      <DefaultRoute name="home" handler={HomeView}/>
    </Route>
);

module.exports = routes;
