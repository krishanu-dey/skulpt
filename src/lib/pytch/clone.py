import copy
from pytch.syscalls import register_sprite_instance


def create_clone_of(original_cls_or_obj):
    """(SPRITE) Create a clone of a SPRITE class or instance

    Two variants, depending on whether the original is a class or an
    instance.  If a class, we clone its instance-0.  If an instance,
    clone that instance.
    """
    if isinstance(original_cls_or_obj, type):
        if not hasattr(original_cls_or_obj, "_pytch_parent_project"):
            raise ValueError("can only clone a Pytch-registered class")

        # Would be surprising if this fails, but handle anyway.
        try:
            obj = original_cls_or_obj.the_original()
        except:
            raise RuntimeError("the_original() failed")

    else:
        obj = original_cls_or_obj

    return create_clone_of_instance(obj)


def create_clone_of_instance(obj):
    new_obj = copy.deepcopy(obj)
    return register_sprite_instance(new_obj, obj)
