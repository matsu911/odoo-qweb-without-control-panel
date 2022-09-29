odoo.define('QWebWithoutControlPanel', function (require) {
  "use strict";

  var viewRegistry = require('web.view_registry');
  var QWebView = require('web.qweb').View;

  var QWebWithoutControlPanel = QWebView.extend({
    withControlPanel: false,
  });

  viewRegistry.add('qweb_without_control_panel', QWebWithoutControlPanel);
});

