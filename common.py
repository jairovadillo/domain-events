from collections import defaultdict


class SubscriberMeta(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        EventBus.subscribe(cls)


class EventBus:
    _subscribers = defaultdict(list)

    @classmethod
    def subscribe(cls, subscriber):
        for event in subscriber.subscribe_to:
            cls._subscribers[event].append(subscriber)

    @classmethod
    def trigger(cls, event):
        for subscriber in cls._subscribers.get(type(event), []):
            subscriber.run(event)
