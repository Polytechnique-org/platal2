'use strict';

/** QuickSearchStore: stores QuickSearch-related data.
 *
 * The stored data is a map of (trimmed) query => list of results.
 */

var Reflux = require('reflux');
var QuickSearchActions = require('../actions.js').QuickSearchActions;
var PlatalAPI = require('../api.js');

var MIN_QUERY_LENGTH = 3;

var quickSearchStore = Reflux.createStore({
  listenables: QuickSearchActions,

  init: function() {
    this.results = {};
  },

  getInitialState: function() {
    return {results: this.results};
  },

  onQuickSearch: function(query) {
    if (this.results[query]) {
      QuickSearchActions.quickSearch.completed({query: query, results: this.results[query]});
    } else if(query.length >= MIN_QUERY_LENGTH) {
      PlatalAPI
        .get('profiles/')
        .query({search: query})
        .then(function(res) {
          QuickSearchActions.quickSearch.completed({query: query, results: res.body.results});
        }, function(error) {
          QuickSearchActions.quickSearch.failed();
        });
    }
  },

  onQuickSearchCompleted: function(reply) {
    this.results[reply['query']] = reply['results'];
    this.trigger(this.results);
  }
});

module.exports = quickSearchStore;
