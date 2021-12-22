"use strict";

const {
    configure_mocha,
    import_deindented,
    pytch_stdout,
    assert,
    assert_float_close,
    one_frame,
    pytch_errors,
} = require("./pytch-testing.js");
configure_mocha();


////////////////////////////////////////////////////////////////////////////////

describe("Glide easing", () => {
    // For "linear", we're only really testing that we've successfully
    // exposed the JavaScript function to Python.  For "ease-in-out",
    // we are also checking the algebra in going from the form given
    // here in the test to the one used in the module.
    [
        {
            easingName: "linear",
            exp_t_fun: t => t,
        },
        {
            easingName: "ease-in-out",
            exp_t_fun: t => ((t < 0.5)
                             ? (2.0 * t * t)
                             : (1.0 - 0.5 * (-2 * t + 2) * (-2 * t + 2))),
        },
    ].forEach(spec => {
        it(`computes ${spec.easingName}`, async () => {
            const project = await import_deindented(`

                import pytch
                import pytch._glide_easing

                cv = pytch._glide_easing.named["${spec.easingName}"]
                print([cv(t / 22.0) for t in range(0, 23)])
            `);

            const got_ts = JSON.parse(pytch_stdout.drain_stdout());
            assert.strictEqual(got_ts.length, 23);

            got_ts.forEach((got_t, idx) => {
                const exp_t = spec.exp_t_fun(idx / 22.0);
                assert_float_close(got_t, exp_t, 1.0e-15);
            });
        });
    });

    it("rejects unknown easing function", async () => {
        const project = await import_deindented(`

            import pytch
            class Banana(pytch.Sprite):
                Costumes = ["yellow-banana.png"]
                @pytch.when_I_receive("run")
                def bad_glide(self):
                    self.glide_to_xy(0, 120, 0.5, "no-such-easing")
        `);
        project.do_synthetic_broadcast("run");
        one_frame(project);
        pytch_errors.assert_sole_error_matches(/not a known kind/);
    });

    it("rejects non-float input", async () => {
        // Only the ease-in-out function actually checks its input.
        const project = await import_deindented(`

            import pytch
            import pytch._glide_easing

            cv = pytch._glide_easing.named["ease-in-out"]
            try:
                cv("hello world")
            except Exception as e:
                print(str(e))
        `);
        assert.strictEqual(
            pytch_stdout.drain_stdout(),
            "input must be float\n"
        );
    });
});
