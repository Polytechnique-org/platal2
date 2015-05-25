'use strict';

// Global imports
var React = require('react');
var Router = require('react-router');

// Globals
var PlatalAPI = require('./api.js');
PlatalAPI.configure({rootUrl: 'http://platal2-demo.polytechnique.org/api/'});

// Routing
var routes = require('./routes.jsx');

Router.run(routes, Router.HistoryLocation, function(Handler) {
  React.render(<Handler/>, document.getElementById('app-content'));
});
