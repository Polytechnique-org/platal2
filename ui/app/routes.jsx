'use strict';

// Global imports
var React = require('react');
var Router = require('react-router');

// Add to JSX scope
var Route = Router.Route;
var DefaultRoute = Router.DefaultRoute;

// Views
var AppView = require('./views/app.jsx');
var HomeView = require('./views/home.jsx');
var InfoView = require('./views/info.jsx');
var QuickSearchView = require('./views/quicksearch.jsx');

var routes = (
    <Route name="app" path="/" handler={AppView}>
      <Route name="info" handler={InfoView}/>
      <Route name="search" handler={QuickSearchView}/>
      <DefaultRoute name="home" handler={HomeView}/>
    </Route>
);

module.exports = routes;
