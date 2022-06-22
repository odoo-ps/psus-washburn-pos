/** @odoo-module **/

import BarcodePickingModel from '@stock_barcode/models/barcode_picking_model';
var rpc = require('web.rpc');
var Class = require('web.Class');

BarcodePickingModel.prototype._putInPack = async function(additionalContext = {}) {
    const context = Object.assign({ barcode_view: true }, additionalContext);
    rpc.query({
            model: 'stock.picking',
            method: 'action_print_slip',
            args: [[], this.params.id],
    }).then(result => {
        if(result){
            this.trigger('do-action', {
                action: result,
            });
        }
    });
    if (!this.groups.group_tracking_lot) {
        return this.notification.add(
            _t("To use packages, enable 'Packages' in the settings"),
            { type: 'danger'}
        );
    }
    await this.save();
    const result = await this.orm.call(
        this.params.model,
        'action_put_in_pack',
        [[this.params.id]],
        { context }
    );
    if (typeof result === 'object') {
        this.trigger('process-action', result);
    } else {
        this.trigger('refresh');
    }
}