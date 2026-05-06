% With framing we use the format frame(Slot, Value).

bird(is_kind_of, animal).
bird(moving_method, fly).
bird(active_at, daylight).
chicken(instance_of, bird).
chicken(moving_method, hover).  % Overrides parent's moving_method

value(Frame, Slot, Value) :-
    Query =.. [Frame, Slot, Value],
    Query, !.

value(Frame, Slot, Value) :-
    parent(Frame, ParentFrame),
    value(ParentFrame, Slot, Value).

parent(Frame, ParentFrame) :-
    (Query =.. [Frame, kind_of, ParentFrame];
    Query =.. [Frame, instance_of, ParentFrame]),
    Query.