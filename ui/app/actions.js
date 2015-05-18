'use strict';

var Reflux = require('reflux');

// Account-related actions
var AccountActions = Reflux.createActions({
  // Setting asyncResult adds .completed and .failed sub-actions.
  "fetchAccount": {asyncResult: true}
});


// Quicksearch-related actions
var QuickSearchActions = Reflux.createActions({
  "quickSearch": {asyncResult: true}
});

// Put other actions here.

module.exports.AccountActions = AccountActions;
module.exports.QuickSearchActions = QuickSearchActions;
