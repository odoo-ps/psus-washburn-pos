odoo.define('signwarehouse_automated_printing.KanbanController', function(require) {
    "use strict";
    var core = require('web.core');
    var KanbanController = require('web.KanbanController');
    var rpc = require('web.rpc');

    KanbanController.include({
        _onAddRecordToColumn: function (ev) {
            var self = this;
            var record = ev.data.record;
            var column = ev.target;
            console.log(record)
            console.log(column)
            if (column.title === 'Completed'){
                rpc.query({
                        model: 'project.task',
                        method: 'action_print_product_label',
                        args: [[], record.id],
                }).then(result => {
                    if(result){
                        this.do_action(result);
                    }
                });
            }
            this.alive(this.model.moveRecord(record.db_id, column.db_id, this.handle))
                .then(function (column_db_ids) {
                    return self._resequenceRecords(column.db_id, ev.data.ids)
                        .then(function () {
                            _.each(column_db_ids, function (db_id) {
                                var data = self.model.get(db_id);
                                self.renderer.updateColumn(db_id, data);
                            });
                        });
                }).guardedCatch(this.reload.bind(this));
        },
    });
});