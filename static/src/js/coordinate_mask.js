/** @odoo-module **/
import { CharField } from "@web/views/fields/char/char_field";
import { registry } from "@web/core/registry";

export class CoordinateMaskWidget extends CharField {
    static template = "web.CharField";

    setup() {
        super.setup();
    }

    async onMounted() {
        super.onMounted();
        const input = this.input.el;
        if (input) {
            const Inputmask = await import('/nap/static/lib/inputmask/dist/inputmask.min.js');
            Inputmask.default({
                mask: "99.999999, -99.999999",
                placeholder: "_",
                showMaskOnHover: false,
                showMaskOnFocus: true,
                greedy: false
            }).mask(input);
        }
    }
}

registry.category("fields").add("coordinate_mask", CoordinateMaskWidget);