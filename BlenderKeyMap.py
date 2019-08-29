keyconfig_data = \
[("Frames",
  {"space_type": 'EMPTY', "region_type": 'WINDOW'},
  {"items":
   [("screen.frame_offset",
     {"type": 'LEFT_ARROW', "value": 'PRESS'},
     {"properties":
      [("delta", -1),
       ],
      },
     ),
    ("screen.frame_offset",
     {"type": 'RIGHT_ARROW', "value": 'PRESS'},
     {"properties":
      [("delta", 1),
       ],
      },
     ),
    ("screen.frame_jump",
     {"type": 'RIGHT_ARROW', "value": 'PRESS', "shift": True},
     {"properties":
      [("end", True),
       ],
      },
     ),
    ("screen.frame_jump",
     {"type": 'LEFT_ARROW', "value": 'PRESS', "shift": True},
     {"properties":
      [("end", False),
       ],
      },
     ),
    ("screen.keyframe_jump",
     {"type": 'UP_ARROW', "value": 'PRESS'},
     {"properties":
      [("next", True),
       ],
      },
     ),
    ("screen.keyframe_jump",
     {"type": 'DOWN_ARROW', "value": 'PRESS'},
     {"properties":
      [("next", False),
       ],
      },
     ),
    ("screen.keyframe_jump",
     {"type": 'MEDIA_LAST', "value": 'PRESS'},
     {"properties":
      [("next", True),
       ],
      },
     ),
    ("screen.keyframe_jump",
     {"type": 'MEDIA_FIRST', "value": 'PRESS'},
     {"properties":
      [("next", False),
       ],
      },
     ),
    ("screen.frame_offset",
     {"type": 'WHEELDOWNMOUSE', "value": 'PRESS', "alt": True},
     {"properties":
      [("delta", 1),
       ],
      },
     ),
    ("screen.frame_offset",
     {"type": 'WHEELUPMOUSE', "value": 'PRESS', "alt": True},
     {"properties":
      [("delta", -1),
       ],
      },
     ),
    ("screen.animation_play",
     {"type": 'SPACE', "value": 'PRESS', "shift": True},
     {    "active":False,
      },
     ),
    ("screen.animation_play",
     {"type": 'SPACE', "value": 'PRESS', "shift": True, "ctrl": True},
     {"properties":
      [("reverse", True),
       ],
    "active":False,
      },
     ),
    ("screen.animation_cancel", {"type": 'ESC', "value": 'PRESS'}, None),
    ("screen.animation_play", {"type": 'MEDIA_PLAY', "value": 'PRESS'}, None),
    ("screen.animation_cancel", {"type": 'MEDIA_STOP', "value": 'PRESS'}, None),
    ],
   },
  ),
 ("Object Mode",
  {"space_type": 'EMPTY', "region_type": 'WINDOW'},
  {"items":
   [("wm.pme_user_pie_menu_call",
     {"type": 'WHEELDOWNMOUSE', "value": 'PRESS', "shift": True, "ctrl": True},
     {"properties":
      [("pie_menu_name", 'Hierarchy Down +'),
       ("invoke_mode", 'HOTKEY'),
       ("keymap", 'Object Mode'),
       ],
      },
     ),
    ("wm.pme_user_pie_menu_call",
     {"type": 'A', "value": 'PRESS', "alt": True},
     {"properties":
      [("pie_menu_name", 'Select Object'),
       ("invoke_mode", 'HOTKEY'),
       ("keymap", 'Object Mode'),
       ],
      },
     ),
    ("wm.pme_user_pie_menu_call",
     {"type": 'WHEELDOWNMOUSE', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("pie_menu_name", 'Hierarchy Down'),
       ("invoke_mode", 'HOTKEY'),
       ("keymap", 'Object Mode'),
       ],
      },
     ),
    ("wm.pme_user_pie_menu_call",
     {"type": 'TAB', "value": 'PRESS', "shift": True, "ctrl": True},
     {"properties":
      [("pie_menu_name", 'Snap Sets'),
       ("invoke_mode", 'HOTKEY'),
       ("keymap", 'Object Mode'),
       ],
      },
     ),
    ("wm.pme_user_pie_menu_call",
     {"type": 'WHEELUPMOUSE', "value": 'PRESS', "shift": True, "ctrl": True},
     {"properties":
      [("pie_menu_name", 'Hierachy Up +'),
       ("invoke_mode", 'HOTKEY'),
       ("keymap", 'Object Mode'),
       ],
      },
     ),
    ("wm.pme_user_pie_menu_call",
     {"type": 'S', "value": 'PRESS', "shift": True},
     {"properties":
      [("pie_menu_name", 'Snap Menu'),
       ("invoke_mode", 'HOTKEY'),
       ("keymap", 'Object Mode'),
       ],
      },
     ),
    ("wm.pme_user_pie_menu_call",
     {"type": 'X', "value": 'PRESS', "alt": True},
     {"properties":
      [("pie_menu_name", 'Mesh: Cut'),
       ("invoke_mode", 'HOTKEY'),
       ("keymap", 'Object Mode'),
       ],
      },
     ),
    ("wm.pme_user_pie_menu_call",
     {"type": 'TAB', "value": 'PRESS'},
     {"properties":
      [("pie_menu_name", 'Modeselektor'),
       ("invoke_mode", 'HOTKEY'),
       ("keymap", 'Object Mode'),
       ],
      },
     ),
    ("wm.pme_user_pie_menu_call",
     {"type": 'MIDDLEMOUSE', "value": 'PRESS'},
     {"properties":
      [("pie_menu_name", 'Visibility Pie Object'),
       ("invoke_mode", 'HOTKEY'),
       ("keymap", 'Object Mode'),
       ],
      },
     ),
    ("wm.pme_user_pie_menu_call",
     {"type": 'WHEELUPMOUSE', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("pie_menu_name", 'Hierachy Up'),
       ("invoke_mode", 'HOTKEY'),
       ("keymap", 'Object Mode'),
       ],
      },
     ),
    ("wm.pme_user_pie_menu_call",
     {"type": 'U', "value": 'PRESS'},
     {"properties":
      [("pie_menu_name", 'UV Viewport'),
       ("invoke_mode", 'HOTKEY'),
       ("keymap", 'Object Mode'),
       ],
      },
     ),
    ("wm.pme_user_pie_menu_call",
     {"type": 'BUTTON4MOUSE', "value": 'PRESS'},
     {"properties":
      [("pie_menu_name", 'Pea Context'),
       ("invoke_mode", 'HOTKEY'),
       ("keymap", 'Object Mode'),
       ],
      },
     ),
    ("wm.call_menu_pie",
     {"type": 'O', "value": 'PRESS', "shift": True},
     {"properties":
      [("name", 'VIEW3D_MT_proportional_editing_falloff_pie'),
       ],
      },
     ),
    ("wm.context_toggle",
     {"type": 'O', "value": 'PRESS'},
     {"properties":
      [("data_path", 'tool_settings.use_proportional_edit_objects'),
       ],
      },
     ),
    ("object.select_all",
     {"type": 'A', "value": 'PRESS'},
     {"properties":
      [("action", 'TOGGLE'),
       ],
      },
     ),
    ("object.select_all",
     {"type": 'A', "value": 'PRESS', "alt": True},
     {"properties":
      [("action", 'DESELECT'),
       ],
      },
     ),
    ("object.select_all",
     {"type": 'I', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("action", 'INVERT'),
       ],
      },
     ),
    ("object.select_more", {"type": 'NUMPAD_PLUS', "value": 'PRESS', "ctrl": True}, None),
    ("object.select_less", {"type": 'NUMPAD_MINUS', "value": 'PRESS', "ctrl": True}, None),
    ("object.select_linked", {"type": 'L', "value": 'PRESS', "shift": True}, None),
    ("object.select_grouped", {"type": 'G', "value": 'PRESS', "shift": True}, None),
    ("object.select_hierarchy",
     {"type": 'LEFT_BRACKET', "value": 'PRESS'},
     {"properties":
      [("direction", 'PARENT'),
       ("extend", False),
       ],
      },
     ),
    ("object.select_hierarchy",
     {"type": 'LEFT_BRACKET', "value": 'PRESS', "shift": True},
     {"properties":
      [("direction", 'PARENT'),
       ("extend", True),
       ],
      },
     ),
    ("object.select_hierarchy",
     {"type": 'RIGHT_BRACKET', "value": 'PRESS'},
     {"properties":
      [("direction", 'CHILD'),
       ("extend", False),
       ],
      },
     ),
    ("object.select_hierarchy",
     {"type": 'RIGHT_BRACKET', "value": 'PRESS', "shift": True},
     {"properties":
      [("direction", 'CHILD'),
       ("extend", True),
       ],
      },
     ),
    ("object.parent_set", {"type": 'P', "value": 'PRESS', "ctrl": True}, None),
    ("object.parent_clear", {"type": 'P', "value": 'PRESS', "alt": True}, None),
    ("object.location_clear",
     {"type": 'G', "value": 'PRESS', "alt": True},
     {"properties":
      [("clear_delta", False),
       ],
      },
     ),
    ("object.rotation_clear",
     {"type": 'R', "value": 'PRESS', "alt": True},
     {"properties":
      [("clear_delta", False),
       ],
      },
     ),
    ("object.scale_clear",
     {"type": 'S', "value": 'PRESS', "alt": True},
     {"properties":
      [("clear_delta", False),
       ],
      },
     ),
    ("object.delete",
     {"type": 'DEL', "value": 'PRESS'},
     {"properties":
      [("use_global", False),
       ],
      },
     ),
    ("object.delete",
     {"type": 'X', "value": 'PRESS', "shift": True},
     {"properties":
      [("use_global", True),
       ],
      },
     ),
    ("object.delete",
     {"type": 'X', "value": 'PRESS'},
     {"properties":
      [("use_global", False),
       ("confirm", False),
       ],
      },
     ),
    ("object.delete",
     {"type": 'DEL', "value": 'PRESS', "shift": True},
     {"properties":
      [("use_global", True),
       ("confirm", False),
       ],
      },
     ),
    ("wm.call_menu",
     {"type": 'A', "value": 'PRESS', "shift": True},
     {"properties":
      [("name", 'VIEW3D_MT_add'),
       ],
      },
     ),
    ("wm.call_menu",
     {"type": 'A', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("name", 'VIEW3D_MT_object_apply'),
       ],
      },
     ),
    ("wm.call_menu",
     {"type": 'L', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("name", 'VIEW3D_MT_make_links'),
       ],
      },
     ),
    ("object.duplicate_move", {"type": 'D', "value": 'PRESS', "shift": True}, None),
    ("object.duplicate_move_linked", {"type": 'D', "value": 'PRESS', "alt": True}, None),
    ("object.join", {"type": 'J', "value": 'PRESS', "ctrl": True}, None),
    ("anim.keyframe_insert_menu", {"type": 'I', "value": 'PRESS'}, None),
    ("anim.keyframe_delete_v3d", {"type": 'I', "value": 'PRESS', "alt": True}, None),
    ("anim.keying_set_active_set", {"type": 'I', "value": 'PRESS', "shift": True, "ctrl": True, "alt": True}, None),
    ("collection.create", {"type": 'G', "value": 'PRESS', "ctrl": True}, None),
    ("collection.objects_remove", {"type": 'G', "value": 'PRESS', "ctrl": True, "alt": True}, None),
    ("collection.objects_remove_all", {"type": 'G', "value": 'PRESS', "shift": True, "ctrl": True, "alt": True}, None),
    ("collection.objects_add_active", {"type": 'G', "value": 'PRESS', "shift": True, "ctrl": True}, None),
    ("collection.objects_remove_active", {"type": 'G', "value": 'PRESS', "shift": True, "alt": True}, None),
    ("wm.call_menu",
     {"type": 'RIGHTMOUSE', "value": 'PRESS'},
     {"properties":
      [("name", 'VIEW3D_MT_object_context_menu'),
       ],
      },
     ),
    ("object.subdivision_set",
     {"type": 'ZERO', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("level", 0),
       ("relative", False),
       ],
      },
     ),
    ("object.subdivision_set",
     {"type": 'ONE', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("level", 1),
       ("relative", False),
       ],
      },
     ),
    ("object.subdivision_set",
     {"type": 'TWO', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("level", 2),
       ("relative", False),
       ],
      },
     ),
    ("object.subdivision_set",
     {"type": 'THREE', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("level", 3),
       ("relative", False),
       ],
      },
     ),
    ("object.subdivision_set",
     {"type": 'FOUR', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("level", 4),
       ("relative", False),
       ],
      },
     ),
    ("object.subdivision_set",
     {"type": 'FIVE', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("level", 5),
       ("relative", False),
       ],
      },
     ),
    ("object.move_to_collection", {"type": 'M', "value": 'PRESS'}, None),
    ("object.link_to_collection", {"type": 'M', "value": 'PRESS', "shift": True}, None),
    ("object.hide_view_clear", {"type": 'H', "value": 'PRESS', "alt": True}, None),
    ("object.hide_view_set",
     {"type": 'H', "value": 'PRESS'},
     {"properties":
      [("unselected", False),
       ],
      },
     ),
    ("object.hide_view_set",
     {"type": 'H', "value": 'PRESS', "shift": True},
     {"properties":
      [("unselected", True),
       ],
      },
     ),
    ("object.hide_collection", {"type": 'H', "value": 'PRESS', "ctrl": True}, None),
    ("object.hide_collection",
     {"type": 'ONE', "value": 'PRESS', "any": True},
     {"properties":
      [("collection_index", 1),
       ],
      },
     ),
    ("object.hide_collection",
     {"type": 'TWO', "value": 'PRESS', "any": True},
     {"properties":
      [("collection_index", 2),
       ],
      },
     ),
    ("object.hide_collection",
     {"type": 'THREE', "value": 'PRESS', "any": True},
     {"properties":
      [("collection_index", 3),
       ],
      },
     ),
    ("object.hide_collection",
     {"type": 'FOUR', "value": 'PRESS', "any": True},
     {"properties":
      [("collection_index", 4),
       ],
      },
     ),
    ("object.hide_collection",
     {"type": 'FIVE', "value": 'PRESS', "any": True},
     {"properties":
      [("collection_index", 5),
       ],
      },
     ),
    ("object.hide_collection",
     {"type": 'SIX', "value": 'PRESS', "any": True},
     {"properties":
      [("collection_index", 6),
       ],
      },
     ),
    ("object.hide_collection",
     {"type": 'SEVEN', "value": 'PRESS', "any": True},
     {"properties":
      [("collection_index", 7),
       ],
      },
     ),
    ("object.hide_collection",
     {"type": 'EIGHT', "value": 'PRESS', "any": True},
     {"properties":
      [("collection_index", 8),
       ],
      },
     ),
    ("object.hide_collection",
     {"type": 'NINE', "value": 'PRESS', "any": True},
     {"properties":
      [("collection_index", 9),
       ],
      },
     ),
    ("object.hide_collection",
     {"type": 'ZERO', "value": 'PRESS', "any": True},
     {"properties":
      [("collection_index", 10),
       ],
      },
     ),
    ],
   },
  ),
 ("3D View",
  {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
  {"items":
   [("wm.pme_user_pie_menu_call",
     {"type": 'LEFTMOUSE', "value": 'DOUBLE_CLICK', "alt": True},
     {"properties":
      [("pie_menu_name", 'View Selected/All'),
       ("invoke_mode", 'HOTKEY'),
       ("keymap", '3D View'),
       ],
      },
     ),
    ("wm.pme_user_pie_menu_call",
     {"type": 'TAB', "value": 'PRESS'},
     {"properties":
      [("pie_menu_name", 'Modeselektor GP'),
       ("invoke_mode", 'HOTKEY'),
       ("keymap", '3D View'),
       ],
      },
     ),
    ("wm.pme_user_pie_menu_call",
     {"type": 'Z', "value": 'PRESS'},
     {"properties":
      [("pie_menu_name", 'Shading Toggle'),
       ("invoke_mode", 'HOTKEY'),
       ("keymap", '3D View'),
       ],
      },
     ),
    ("wm.pme_user_pie_menu_call",
     {"type": 'Z', "value": 'PRESS'},
     {"properties":
      [("pie_menu_name", 'Shading Menu 1'),
       ("invoke_mode", 'HOTKEY'),
       ("keymap", '3D View'),
       ],
      },
     ),
    ("wm.pme_user_pie_menu_call",
     {"type": 'Z', "value": 'PRESS', "shift": True},
     {"properties":
      [("pie_menu_name", 'Shading Menu 2'),
       ("invoke_mode", 'HOTKEY'),
       ("keymap", '3D View'),
       ],
      },
     ),
    ("bc.topbar_activate", {"type": 'W', "value": 'PRESS', "alt": True}, None),
    ("view3d.cursor3d", {"type": 'RIGHTMOUSE', "value": 'PRESS', "shift": True}, None),
    ("transform.translate",
     {"type": 'EVT_TWEAK_R', "value": 'ANY', "shift": True},
     {"properties":
      [("cursor_transform", True),
       ("release_confirm", True),
       ],
      },
     ),
    ("view3d.localview", {"type": 'NUMPAD_SLASH', "value": 'PRESS'}, None),
    ("view3d.localview", {"type": 'SLASH', "value": 'PRESS'}, None),
    ("view3d.localview_remove_from", {"type": 'M', "value": 'PRESS'}, None),
    ("view3d.rotate", {"type": 'LEFTMOUSE', "value": 'PRESS', "alt": True}, None),
    ("view3d.move", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "alt": True}, None),
    ("view3d.zoom", {"type": 'RIGHTMOUSE', "value": 'PRESS', "alt": True}, None),
    ("view3d.dolly", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "shift": True, "ctrl": True}, None),
    ("view3d.view_selected",
     {"type": 'NUMPAD_PERIOD', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("use_all_regions", True),
       ],
      },
     ),
    ("view3d.view_selected",
     {"type": 'NUMPAD_PERIOD', "value": 'PRESS'},
     {"properties":
      [("use_all_regions", False),
       ],
      },
     ),
    ("view3d.smoothview", {"type": 'TIMER1', "value": 'ANY', "any": True}, None),
    ("view3d.rotate", {"type": 'TRACKPADPAN', "value": 'ANY'}, None),
    ("view3d.rotate", {"type": 'MOUSEROTATE', "value": 'ANY'}, None),
    ("view3d.move", {"type": 'TRACKPADPAN', "value": 'ANY', "shift": True}, None),
    ("view3d.zoom", {"type": 'TRACKPADZOOM', "value": 'ANY'}, None),
    ("view3d.zoom", {"type": 'TRACKPADPAN', "value": 'ANY', "ctrl": True}, None),
    ("view3d.zoom",
     {"type": 'NUMPAD_PLUS', "value": 'PRESS'},
     {"properties":
      [("delta", 1),
       ],
      },
     ),
    ("view3d.zoom",
     {"type": 'NUMPAD_MINUS', "value": 'PRESS'},
     {"properties":
      [("delta", -1),
       ],
      },
     ),
    ("view3d.zoom",
     {"type": 'EQUAL', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("delta", 1),
       ],
      },
     ),
    ("view3d.zoom",
     {"type": 'MINUS', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("delta", -1),
       ],
      },
     ),
    ("view3d.zoom",
     {"type": 'WHEELINMOUSE', "value": 'PRESS'},
     {"properties":
      [("delta", 1),
       ],
      },
     ),
    ("view3d.zoom",
     {"type": 'WHEELOUTMOUSE', "value": 'PRESS'},
     {"properties":
      [("delta", -1),
       ],
      },
     ),
    ("view3d.dolly",
     {"type": 'NUMPAD_PLUS', "value": 'PRESS', "shift": True},
     {"properties":
      [("delta", 1),
       ],
      },
     ),
    ("view3d.dolly",
     {"type": 'NUMPAD_MINUS', "value": 'PRESS', "shift": True},
     {"properties":
      [("delta", -1),
       ],
      },
     ),
    ("view3d.dolly",
     {"type": 'EQUAL', "value": 'PRESS', "shift": True, "ctrl": True},
     {"properties":
      [("delta", 1),
       ],
      },
     ),
    ("view3d.dolly",
     {"type": 'MINUS', "value": 'PRESS', "shift": True, "ctrl": True},
     {"properties":
      [("delta", -1),
       ],
      },
     ),
    ("view3d.view_center_camera", {"type": 'HOME', "value": 'PRESS'}, None),
    ("view3d.view_center_lock", {"type": 'HOME', "value": 'PRESS'}, None),
    ("view3d.view_all",
     {"type": 'HOME', "value": 'PRESS'},
     {"properties":
      [("center", False),
       ],
      },
     ),
    ("view3d.view_all",
     {"type": 'HOME', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("use_all_regions", True),
       ("center", False),
       ],
      },
     ),
    ("view3d.view_all",
     {"type": 'C', "value": 'PRESS', "shift": True},
     {"properties":
      [("center", True),
       ],
      },
     ),
    ("wm.call_menu_pie",
     {"type": 'ACCENT_GRAVE', "value": 'CLICK_DRAG'},
     {"properties":
      [("name", 'VIEW3D_MT_view_pie'),
       ],
      },
     ),
    ("view3d.navigate", {"type": 'ACCENT_GRAVE', "value": 'CLICK'}, None),
    ("view3d.navigate", {"type": 'ACCENT_GRAVE', "value": 'PRESS', "shift": True}, None),
    ("view3d.view_camera", {"type": 'NUMPAD_0', "value": 'PRESS'}, None),
    ("view3d.view_axis",
     {"type": 'NUMPAD_1', "value": 'PRESS'},
     {"properties":
      [("type", 'FRONT'),
       ],
      },
     ),
    ("view3d.view_orbit",
     {"type": 'NUMPAD_2', "value": 'PRESS'},
     {"properties":
      [("type", 'ORBITDOWN'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_3', "value": 'PRESS'},
     {"properties":
      [("type", 'RIGHT'),
       ],
      },
     ),
    ("view3d.view_orbit",
     {"type": 'NUMPAD_4', "value": 'PRESS'},
     {"properties":
      [("type", 'ORBITLEFT'),
       ],
      },
     ),
    ("view3d.view_persportho", {"type": 'NUMPAD_5', "value": 'PRESS'}, None),
    ("view3d.view_orbit",
     {"type": 'NUMPAD_6', "value": 'PRESS'},
     {"properties":
      [("type", 'ORBITRIGHT'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_7', "value": 'PRESS'},
     {"properties":
      [("type", 'TOP'),
       ],
      },
     ),
    ("view3d.view_orbit",
     {"type": 'NUMPAD_8', "value": 'PRESS'},
     {"properties":
      [("type", 'ORBITUP'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_1', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("type", 'BACK'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_3', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("type", 'LEFT'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_7', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("type", 'BOTTOM'),
       ],
      },
     ),
    ("view3d.view_pan",
     {"type": 'NUMPAD_2', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("type", 'PANDOWN'),
       ],
      },
     ),
    ("view3d.view_pan",
     {"type": 'NUMPAD_4', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("type", 'PANLEFT'),
       ],
      },
     ),
    ("view3d.view_pan",
     {"type": 'NUMPAD_6', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("type", 'PANRIGHT'),
       ],
      },
     ),
    ("view3d.view_pan",
     {"type": 'NUMPAD_8', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("type", 'PANUP'),
       ],
      },
     ),
    ("view3d.view_roll",
     {"type": 'NUMPAD_4', "value": 'PRESS', "shift": True},
     {"properties":
      [("type", 'LEFT'),
       ],
      },
     ),
    ("view3d.view_roll",
     {"type": 'NUMPAD_6', "value": 'PRESS', "shift": True},
     {"properties":
      [("type", 'RIGHT'),
       ],
      },
     ),
    ("view3d.view_orbit",
     {"type": 'NUMPAD_9', "value": 'PRESS'},
     {"properties":
      [("angle", 3.1415927),
       ("type", 'ORBITRIGHT'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_1', "value": 'PRESS', "shift": True},
     {"properties":
      [("type", 'FRONT'),
       ("align_active", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_3', "value": 'PRESS', "shift": True},
     {"properties":
      [("type", 'RIGHT'),
       ("align_active", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_7', "value": 'PRESS', "shift": True},
     {"properties":
      [("type", 'TOP'),
       ("align_active", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_1', "value": 'PRESS', "shift": True, "ctrl": True},
     {"properties":
      [("type", 'BACK'),
       ("align_active", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_3', "value": 'PRESS', "shift": True, "ctrl": True},
     {"properties":
      [("type", 'LEFT'),
       ("align_active", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_7', "value": 'PRESS', "shift": True, "ctrl": True},
     {"properties":
      [("type", 'BOTTOM'),
       ("align_active", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'EVT_TWEAK_M', "value": 'NORTH', "alt": True},
     {"properties":
      [("type", 'TOP'),
       ("relative", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'EVT_TWEAK_M', "value": 'SOUTH', "alt": True},
     {"properties":
      [("type", 'BOTTOM'),
       ("relative", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'EVT_TWEAK_M', "value": 'EAST', "alt": True},
     {"properties":
      [("type", 'RIGHT'),
       ("relative", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'EVT_TWEAK_M', "value": 'WEST', "alt": True},
     {"properties":
      [("type", 'LEFT'),
       ("relative", True),
       ],
      },
     ),
    ("view3d.view_center_pick", {"type": 'MIDDLEMOUSE', "value": 'CLICK', "alt": True}, None),
    ("view3d.ndof_orbit_zoom", {"type": 'NDOF_MOTION', "value": 'ANY'}, None),
    ("view3d.ndof_orbit", {"type": 'NDOF_MOTION', "value": 'ANY', "ctrl": True}, None),
    ("view3d.ndof_pan", {"type": 'NDOF_MOTION', "value": 'ANY', "shift": True}, None),
    ("view3d.ndof_all", {"type": 'NDOF_MOTION', "value": 'ANY', "shift": True, "ctrl": True}, None),
    ("view3d.view_selected",
     {"type": 'NDOF_BUTTON_FIT', "value": 'PRESS'},
     {"properties":
      [("use_all_regions", False),
       ],
      },
     ),
    ("view3d.view_roll",
     {"type": 'NDOF_BUTTON_ROLL_CCW', "value": 'PRESS'},
     {"properties":
      [("type", 'LEFT'),
       ],
      },
     ),
    ("view3d.view_roll",
     {"type": 'NDOF_BUTTON_ROLL_CCW', "value": 'PRESS'},
     {"properties":
      [("type", 'RIGHT'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NDOF_BUTTON_FRONT', "value": 'PRESS'},
     {"properties":
      [("type", 'FRONT'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NDOF_BUTTON_BACK', "value": 'PRESS'},
     {"properties":
      [("type", 'BACK'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NDOF_BUTTON_LEFT', "value": 'PRESS'},
     {"properties":
      [("type", 'LEFT'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NDOF_BUTTON_RIGHT', "value": 'PRESS'},
     {"properties":
      [("type", 'RIGHT'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NDOF_BUTTON_TOP', "value": 'PRESS'},
     {"properties":
      [("type", 'TOP'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NDOF_BUTTON_BOTTOM', "value": 'PRESS'},
     {"properties":
      [("type", 'BOTTOM'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NDOF_BUTTON_FRONT', "value": 'PRESS', "shift": True},
     {"properties":
      [("type", 'FRONT'),
       ("align_active", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NDOF_BUTTON_RIGHT', "value": 'PRESS', "shift": True},
     {"properties":
      [("type", 'RIGHT'),
       ("align_active", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NDOF_BUTTON_TOP', "value": 'PRESS', "shift": True},
     {"properties":
      [("type", 'TOP'),
       ("align_active", True),
       ],
      },
     ),
    ("view3d.select",
     {"type": 'LEFTMOUSE', "value": 'CLICK'},
     {"properties":
      [("deselect_all", True),
       ],
      },
     ),
    ("view3d.select",
     {"type": 'LEFTMOUSE', "value": 'CLICK', "shift": True},
     {"properties":
      [("toggle", True),
       ],
      },
     ),
    ("view3d.select",
     {"type": 'LEFTMOUSE', "value": 'CLICK', "ctrl": True},
     {"properties":
      [("center", True),
       ("object", True),
       ],
      },
     ),
    ("view3d.select",
     {"type": 'LEFTMOUSE', "value": 'CLICK', "alt": True},
     {"properties":
      [("enumerate", True),
       ],
      },
     ),
    ("view3d.select",
     {"type": 'LEFTMOUSE', "value": 'CLICK', "shift": True, "ctrl": True},
     {"properties":
      [("extend", True),
       ("toggle", True),
       ("center", True),
       ],
      },
     ),
    ("view3d.select",
     {"type": 'LEFTMOUSE', "value": 'CLICK', "ctrl": True, "alt": True},
     {"properties":
      [("center", True),
       ("enumerate", True),
       ],
      },
     ),
    ("view3d.select",
     {"type": 'LEFTMOUSE', "value": 'CLICK', "shift": True, "alt": True},
     {"properties":
      [("toggle", True),
       ("enumerate", True),
       ],
      },
     ),
    ("view3d.select",
     {"type": 'LEFTMOUSE', "value": 'CLICK', "shift": True, "ctrl": True, "alt": True},
     {"properties":
      [("toggle", True),
       ("center", True),
       ("enumerate", True),
       ],
      },
     ),
    ("view3d.select_box", {"type": 'B', "value": 'PRESS'}, None),
    ("view3d.select_lasso",
     {"type": 'EVT_TWEAK_R', "value": 'ANY', "ctrl": True},
     {"properties":
      [("mode", 'ADD'),
       ],
      },
     ),
    ("view3d.select_lasso",
     {"type": 'EVT_TWEAK_R', "value": 'ANY', "shift": True, "ctrl": True},
     {"properties":
      [("mode", 'SUB'),
       ],
      },
     ),
    ("view3d.select_circle", {"type": 'C', "value": 'PRESS'}, None),
    ("view3d.clip_border", {"type": 'B', "value": 'PRESS', "alt": True}, None),
    ("view3d.zoom_border", {"type": 'B', "value": 'PRESS', "shift": True}, None),
    ("view3d.render_border", {"type": 'B', "value": 'PRESS', "ctrl": True}, None),
    ("view3d.clear_render_border", {"type": 'B', "value": 'PRESS', "ctrl": True, "alt": True}, None),
    ("view3d.camera_to_view", {"type": 'NUMPAD_0', "value": 'PRESS', "ctrl": True, "alt": True}, None),
    ("view3d.object_as_camera", {"type": 'NUMPAD_0', "value": 'PRESS', "ctrl": True}, None),
    ("view3d.copybuffer", {"type": 'C', "value": 'PRESS', "ctrl": True}, None),
    ("view3d.pastebuffer", {"type": 'V', "value": 'PRESS', "ctrl": True}, None),
    ("transform.translate", {"type": 'G', "value": 'PRESS'}, None),
    ("transform.translate", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None),
    ("transform.rotate", {"type": 'R', "value": 'PRESS'}, None),
    ("transform.resize", {"type": 'S', "value": 'PRESS'}, None),
    ("transform.bend", {"type": 'W', "value": 'PRESS', "shift": True}, None),
    ("transform.tosphere", {"type": 'S', "value": 'PRESS', "shift": True, "alt": True}, None),
    ("transform.shear", {"type": 'S', "value": 'PRESS', "shift": True, "ctrl": True, "alt": True}, None),
    ("transform.mirror", {"type": 'M', "value": 'PRESS', "ctrl": True}, None),
    ("wm.context_toggle",
     {"type": 'TAB', "value": 'PRESS', "shift": True},
     {"properties":
      [("data_path", 'tool_settings.use_snap'),
       ],
      },
     ),
    ("wm.call_panel",
     {"type": 'TAB', "value": 'PRESS', "shift": True, "ctrl": True},
     {"properties":
      [("name", 'VIEW3D_PT_snapping'),
       ("keep_open", False),
       ],
      },
     ),
    ("object.transform_axis_target", {"type": 'T', "value": 'PRESS', "shift": True}, None),
    ("transform.skin_resize", {"type": 'A', "value": 'PRESS', "ctrl": True}, None),
    ("wm.call_menu_pie",
     {"type": 'S', "value": 'PRESS', "shift": True},
     {"properties":
      [("name", 'VIEW3D_MT_snap_pie'),
       ],
      },
     ),
    ("wm.context_toggle",
     {"type": 'ACCENT_GRAVE', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("data_path", 'space_data.show_gizmo_context'),
       ],
      },
     ),
    ("wm.call_menu_pie",
     {"type": 'PERIOD', "value": 'PRESS'},
     {"properties":
      [("name", 'VIEW3D_MT_pivot_pie'),
       ],
      },
     ),
    ("wm.call_menu_pie",
     {"type": 'COMMA', "value": 'PRESS'},
     {"properties":
      [("name", 'VIEW3D_MT_orientations_pie'),
       ],
      },
     ),
    ("wm.call_menu_pie",
     {"type": 'Z', "value": 'CLICK_DRAG'},
     {"properties":
      [("name", 'VIEW3D_MT_shading_ex_pie'),
       ],
      },
     ),
    ("view3d.toggle_shading",
     {"type": 'Z', "value": 'CLICK'},
     {"properties":
      [("type", 'WIREFRAME'),
       ],
      },
     ),
    ("view3d.toggle_shading",
     {"type": 'Z', "value": 'PRESS', "shift": True},
     {"properties":
      [("type", 'WIREFRAME'),
       ],
      },
     ),
    ("view3d.toggle_xray", {"type": 'Z', "value": 'PRESS', "alt": True}, None),
    ("wm.context_toggle",
     {"type": 'Z', "value": 'PRESS', "shift": True, "alt": True},
     {"properties":
      [("data_path", 'space_data.overlay.show_overlays'),
       ],
      },
     ),
    ("wm.tool_set_by_id",
     {"type": 'W', "value": 'PRESS'},
     {"properties":
      [("name", 'builtin.select_box'),
       ("cycle", True),
       ],
      },
     ),
    ],
   },
  ),
 ]


if __name__ == "__main__":
    import os
    from bl_keymap_utils.io import keyconfig_import_from_data
    keyconfig_import_from_data(os.path.splitext(os.path.basename(__file__))[0], keyconfig_data)
