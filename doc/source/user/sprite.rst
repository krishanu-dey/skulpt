Sprites
-------

Sprites are the things in a project that appear on the stage, move
about, and generally perform actions. Most projects will have at least
one sprite.

You control how a sprite moves and acts by writing *scripts*. Each
sprite can also have *costumes* and *sounds* that control how it looks
and sounds.

Each sprite has *methods* which are commands that you can issue to get a
sprite to do something.  You also write your own methods to say how your
sprite should behave, in two ways:

* A method which should run every time some event happens, for example
  when the green flag is clicked.  See :doc:`hat-blocks` for details of
  how this works.
* A method which your code will use internally.  These are the
  equivalent of the *custom blocks* you can define in Scratch.


Creating Sprites
~~~~~~~~~~~~~~~~

You can create a Sprite in your project by declaring a Python *class*
that uses the Sprite as a foundation. You do this by creating a class
with some name (for example, "Kitten"), and mentioning the pytch Sprite
class as its basis. Here is an example of a Kitten class that has a
single costume (costumes are discussed just below):

.. code-block:: python

   import pytch

   class Kitten(pytch.Sprite):
       Costumes = ["happy-kitten.jpg"]


Saying how a sprite should behave
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In Scratch you put together scripts which say how you want your Sprite
to behave when certain things happen, for example, when that Sprite is
clicked.  In Pytch, you do this by writing your own methods on your
class.  For example,

.. code:: python

   import pytch

   class Spaceship(pytch.Sprite):
       @pytch.when_key_pressed("ArrowUp")
       def move_up(self):
           self.change_y(10)

Here we see:

* The *method decorator* ``pytch.when_key_pressed`` does the job of a
  Scratch *hat block* — Pytch's decorators are described in :doc:`their
  own section of the documentation<hat-blocks>`.
* The method call ``self.change_y(10)`` does the job of the *change y by*
  Scratch block — a Pytch sprite's methods are described below.


Controlling how a sprite looks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each sprite can have a collection of *Costumes* that control how it
looks. The first costume mentioned will be how the sprite first appears
and you can change the Sprite's appearance using commands.

If a Sprite is to appear on the stage then it has to have at least one
costume (it's OK for a sprite to be invisible, and then it doesn't need
to have any costumes at all). Costumes are controlled by a variable in
each Sprite that lists the images that the Sprite can have. To use an
image you have to upload it to your project, and then you can add it to
your Sprite's list of available Costumes.

You can read the details of how you list costumes in the
:ref:`assets<costume_specifications>` document.

Usually all you have to do is make a list called *Costumes* in the
sprite and list all the names of the uploaded files you want to use.

This list has to be set up as the Sprite is created (Pytch can't yet
load more images after the sprite has been set up).

The *Costumes* variable needs to be declared inside the Sprite. For
example, here is a definition for a new Sprite class that will have two
costumes:

.. code-block:: python

   class Kitten(pytch.Sprite):
       Costumes = ["smiling-kitten.jpg",
                   "frowning-kitten.jpg"]

By default the Sprite will use the first image as its appearance. If you
want to change to another costume you can use the ``switch_costume()``
method.


Setting the sprite size
  .. function:: self.set_size(size)

     Set how large the sprite appears, as a proportion of the size of the
     current costume image, where ``1`` is the normal size of the image.
     For example, ``self.set_size(0.5)`` will set the sprite to be
     half-sized.

Finding out the sprite's size
  .. attribute:: self.size

     The current size of the Sprite, where ``1`` is normal size,
     ``0.5`` is half-size, ``2`` is double-size, and so on.

Showing and hiding the sprite
  .. function:: self.show()
                self.hide()

     Make the sprite appear or disappear from the stage. Sprites that are
     not showing can still be moved, change costume, and so on but you
     won't see the effect until the sprite is shown again.

Changing the sprite appearance
  .. function:: self.switch_costume(name)

     Select one of the costumes listed in this Sprite's *Costumes*
     variable. The name is the costume's *label*, which is usually the
     filename without the extension (see
     :doc:`costume-specs` for full details). For
     example, you might use ``self.switch_costume("smiling-kitten")`` to
     choose a new costume.

  .. function:: self.switch_costume(costume_number)
     :noindex:

     Select one of the costumes listed in this Sprite's *Costumes*
     variable, by number.  Python starts counting entries in lists *at
     zero*, so to switch to the first costume, you would use
     ``self.switch_costume(0)``; to switch to the second costume, you would
     use ``self.switch_costume(1)``, and so on.

  .. function:: self.next_costume()

     Switch to the costume after the current one.  If the Sprite is wearing
     the last costume in its ``Costumes`` list, then go back to the first
     one in the list.

  .. function:: self.next_costume(n_steps)
     :noindex:

     Switch to the costume ``n_steps`` after the current one.  If this
     would take the Sprite beyond the end of its ``Costumes`` list, then
     wrap round to the first entry again, as if the costumes were in a
     circle.  You can use a negative number for ``n_steps`` to choose an
     *earlier* costume in the list.  For example, ``self.next_costume(-1)``
     will switch to the *previous* costume.

Finding out what costume the Sprite is currently wearing
  .. attribute:: self.costume_number

     The *zero-based* number of the costume currently being worn by the
     Sprite.  Here, 'zero-based' means that the first costume in the
     ``Costumes`` list is number 0; the second costume is number 1; and so
     on.  This is the way that Python refers to list elements.

  .. attribute:: self.costume_name

     The name of the costume currently being worn by the Sprite.

Controlling the order Sprites are drawn
  When one sprite overlaps another it is the order that they are drawn
  that controls what you see. Sprites on the back layer are drawn first,
  and then Sprites from the next layer are drawn on top of that, and so
  on until the front layer is reached. By moving sprites between layers
  you can control which Sprites appear on top.

  .. function:: self.go_to_front_layer()
                self.go_to_back_layer()

     These methods move a sprite to the very front or the very back of the
     layers.

  .. function:: self.go_forward_layers(n)
                self.go_backward_layers(n)

     These methods move a sprite a certain number of layers forward or
     backward.


Moving a Sprite
~~~~~~~~~~~~~~~

Sprites can move their position on the stage using these motion
commands. There is an exact x and y position on the stage where the
"origin" of the sprite is. Normally the origin in the exact middle of
the sprite's current costume, but you can change the origin when you are
creating the costume (see
:ref:`here<costume_label_origin_specifications>`)

.. function:: self.go_to_xy(x, y)

   Move the sprite to a particular position on the stage.

.. function:: self.glide_to_xy(x, y, seconds)

   Glide the sprite smoothly to a particular position on the stage, taking
   the given number of seconds to do so.  The value for ``seconds`` does
   not have to be a whole number.  *Advanced/experimental:* You can also
   give a fourth argument, to give the *easing* of the glide.  This can
   be: the string ``"linear"``, to move at a constant speed; or the string
   ``ease-in-out``, to start slowly, speed up, then slow back down as the
   glide finishes.

.. function:: self.change_x(dx)

   Change the x-position of the sprite by a certain amount (for example,
   ``self.change_x(10)`` will move the sprite 10 pixels to the right on the
   stage). The number of pixels can be negative.

.. function:: self.change_y(dy)

   Change the y-position of the sprite by a certain amount (for example,
   ``self.change_y(10)`` will move the sprite 10 pixels up on the
   stage). The number can be negative.

.. function:: self.set_x(x)

   Move the sprite to a certain x-position on the stage while keeping its
   y-position the same.

.. function:: self.set_y(y)

   Move the sprite to a certain y-position on the stage while keeping its
   x-position the same.


Finding a Sprite's position
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attribute:: self.x_position
               self.y_position

   The current *x* or *y* position of the sprite.  These are
   *properties*, so you do not use ``()`` after them.


Turning a Sprite
~~~~~~~~~~~~~~~~

A sprite can turn round and point in different directions.

.. warning::

   This feature is experimental.  Currently, the ``touching()``
   results (see :ref:`collision_detection`) will be inaccurate if a
   sprite has turned from its starting direction.  Also,
   ``when_this_sprite_clicked`` events will not be accurately
   detected.

.. function:: self.turn_degrees(angle)

   Turn the sprite by the given angle (measured in degrees), in an
   anticlockwise (counter-clockwise) direction.  To turn clockwise,
   use a negative value for ``angle``.  This is the opposite
   convention to Scratch, but "positive is anticlockwise" is the
   common mathematical convention, so Pytch uses it.

.. function:: self.point_degrees(angle)

   Turn the sprite so it is pointing in the direction of the given
   angle (measured in degrees).  An angle of zero means that the
   sprite is drawn the same way up as the original image for the
   costume it's currently wearing.  An angle of 90° means the sprite
   points a quarter-turn anticlockwise (counter-clockwise) from its
   original image.  To point a quarter-turn clockwise, use −90° (or
   270°, which comes to the same thing).

.. attribute:: self.direction

   The direction the sprite is currently pointing, measured in
   degrees.


.. _methods_playing_sounds:

Making sounds
~~~~~~~~~~~~~

Sounds have to be loaded into the Sprite when it is created (see
:doc:`sound-specs`). Once a sound has been loaded you can get the
sprite to play it.

.. function:: self.start_sound(sound_name)

   Start a sound playing. You refer to the sound using its *label*, which
   is usually the filename without the extension (see :doc:`sound-specs`
   for full details). Once the sound has started the Sprite will move on
   to its next instruction.

.. function:: self.play_sound_until_done(sound_name)

   Start a sound playing. You can refer to the sound using its *label*,
   as for ``start_sound()``. This method will not return until the entire
   sound has played, so the script it is contained in won't do its next
   instruction until then.


Making and deleting copies of a Sprite
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each Sprite is created on the Stage at the start of the program, but it
is possible to create further copies of each Sprite when the program is
running. These copies are called "clones" of the original.

When a clone is created it starts at the same position and wearing the
same costume as the original, but it can run its own scripts to change
its behaviour. The "self" variable always refers to the *current* clone.

Creating new clones
^^^^^^^^^^^^^^^^^^^

Clones can be created using the ``pytch.create_clone_of(thing)``
function:

.. function:: pytch.create_clone_of(thing)

   Create a new clone of ``thing``.  You can create clones in two ways.
   You can clone the original or a copy of one of your Sprites, for example
   the copy which is calling the ``create_clone_of()`` function:

   .. code-block:: python

      pytch.create_clone_of(self)

   Or you can create a clone of a particular class of Sprite:

   .. code-block:: python

      pytch.create_clone_of(Spaceship)

   In this case, Pytch makes a clone of the original instance of that
   sprite.

Deleting clones
^^^^^^^^^^^^^^^

.. function:: self.delete_this_clone()

   Remove the current clone. If this method is run by the original sprite
   then it has no effect, but if it is run by a clone then the clone
   immediately vanishes.

Finding existing clones
^^^^^^^^^^^^^^^^^^^^^^^

.. function:: Class.the_original()

   This returns a reference to the *original* object that this clone is a
   copy of. This can be used to look up variables or send messages to the
   original object. If it is run by the original Sprite then it returns a
   reference to itself. Notice that this method is run using the class name
   (for example ``Kitten.the_original()``), not the ``self`` object.

.. function:: Class.all_clones()

   Returns a list of all the existing clones of the Sprite that is
   mentioned (for example ``Kitten.all_clones()``). Notice that this method
   is run using the class name (for example ``Kitten.all_clones()``), not
   the ``self`` object.

.. function:: Class.all_instances()

   Like ``all_clones``, this returns a list of all clones of the Sprite
   that is mentioned (for example ``Kitten.all_clones()``), but
   ``all_instances`` also includes the original Sprite in the list. This is
   useful if you want access to everything (both clones and
   originals). Notice that this method is run using the class name (for
   example ``Kitten.all_instances()``), not the ``self`` object.


.. _collision_detection:

Checking for sprites colliding
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. function:: self.touching(target_class)

   You can use this method to check whether this sprite is touching any
   instance of another class. For example ``self.touching(Dog)`` will
   return either True or False depending on whether the current Sprite is
   overlapping a ``Dog`` sprite.

   At the moment Pytch does not look at the actual image in the costume,
   just its overall size, so if the two costumes have blank sections but
   the costumes themselves are overlapping then this method will still
   return true. The current costume and the size set by ``set_size`` is
   taken into account when checking.

   Note that you check using a *class* name, so if the ``self`` sprite is
   touching any clone of the target class then ``touching`` will return
   true.


Showing and hiding speech bubbles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Speech bubbles can be used to get Sprites to show some text on the
Stage.

.. function:: self.say(content)

   Show a speech bubble next to the current Sprite, showing the text
   supplied. For exampler ``self.say("Hello there")``.  If the Sprite uses
   ``self.hide()`` to disappear from the stage then the bubble will also
   disappear.  If the Sprite then re-appears (by using ``self.show()``),
   then the speech bubble will also re-appear.

   To remove a Sprite's speech bubble, use the empty string for the
   ``content`` argument, as in:

   .. code-block:: python

      # Remove speech bubble:
      self.say("")

.. function:: self.say_for_seconds(content, seconds)

   Show a speech balloon, wait for the number of seconds given, and then
   remove it. The whole script will wait while the balloon is being shown.
   If a second script calls ``say_for_seconds()`` while a first script is
   already in the middle of ``say_for_seconds()``, the second script's
   speech replaces the first script's speech.


Asking the user a question
~~~~~~~~~~~~~~~~~~~~~~~~~~

Pytch has a method matching Scratch's *ask and wait* block.  In
Scratch, you can find what the user typed using the *answer* reporter
block.  In Pytch, the user's answer is *returned* to your program from
the ``ask_and_wait()`` method.

.. function:: self.ask_and_wait(question)

   Ask the *question*, and pop up an input box where the user can type
   their answer.  If the Sprite is currently shown, the question is
   asked with a speech bubble.  If the Sprite is hidden, the question is
   asked as part of the input box.

   Your method is paused while the user is typing their answer, and will
   continue once the user submits their answer.  The answer is returned,
   so you will usually assign it to a variable.  For example, this code
   assigns the user's answer to a variable ``name`` and then greets the
   user:

   .. code:: python

      class Banana(pytch.Sprite):
          # [ ... Costumes, Sounds, other methods, etc. ... ]
          @pytch.when_this_sprite_clicked
          def ask_user_their_name(self):
              name = self.ask_and_wait("What's your name?")
              self.say(f"Hello, {name}!")
