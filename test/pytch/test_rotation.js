"use strict";

const {
    configure_mocha,
    import_deindented,
    assert_float_close,
    assert_renders_as,
    one_frame,
} = require("./pytch-testing.js");
configure_mocha();


////////////////////////////////////////////////////////////////////////////////
//
// Sprite rotation

describe("Sprite rotation", () => {
    it("can turn and point", async () => {
        const project = await import_deindented(`

            import pytch
            class Banana(pytch.Sprite):
                Costumes = ["yellow-banana.png"]
                @pytch.when_I_receive("turn")
                def turn(self):
                    self.turn_degrees(41)
                @pytch.when_I_receive("point")
                def point(self):
                    self.point_degrees(102)
        `);

        const banana = project.instance_0_by_class_name("Banana");

        const assert_direction = (msg, exp_direction) => {
            project.do_synthetic_broadcast(msg)
            one_frame(project);
            const got_direction = banana.js_attr("direction");
            assert_float_close(got_direction, exp_direction, 0.001);
        };

        assert_direction("turn", 41);
        assert_direction("turn", 82);
        assert_direction("point", 102);
        assert_direction("turn", 143);

        // Check all new parts of the rendering instruction:
        //     rotation, image-cx, image-cy
        assert_renders_as(
            "final",
            project,
            [["RenderImage", 0, 0, 1, "yellow-banana", 143, 40, 15]]
        );
    });
});
