'use strict';

var Reflux = require('reflux');

// Account-related actions
var AccountActions = Reflux.createActions({
    // Setting asyncResult adds .completed and .failed sub-actions.
    "fetchAccount": {asyncResult: true}
});

// Put other actions here.

module.exports = AccountActions;
