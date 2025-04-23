import asyncio

# Asynchronous Observer Pattern Example
class BirdObserver:
    def __init__(self, bird):
        self.bird = bird

    async def notify_observer(self, predator):
        print(f"{self.bird} sees the {predator}")
        await asyncio.sleep(1)
        print(f"{self.bird} is now safe")

class SentinalBird:
    def __init__(self):
        self.observers = []

    def register_observer(self, observer):
        self.observers.append(observer)

    async def spot_predator(self, predator):

        print(f"Sentinal bird sees the {predator}")
        tasks = [observer.notify_observer(predator) for observer in self.observers]
        await asyncio.gather(*tasks)


async def main():
    sentinal1 = SentinalBird()

    sentinal1.register_observer(BirdObserver("sparrow"))
    sentinal1.register_observer(BirdObserver("finch"))
    sentinal1.register_observer(BirdObserver("robin"))

    await sentinal1.spot_predator("hawk")

if __name__ == "__main__":
    asyncio.run(main())


# # Synchronous Observer Pattern Example
# class BirdObserver:
#     def __init__(self, bird):
#         self.bird = bird

#     def notify_observer(self, predator):
#         print(f"{self.bird} sees the {predator}")

# class SentinalBird:
#     def __init__(self):
#         self.observers = []

#     def register_observer(self, observer):
#         self.observers.append(observer)

#     def spot_predator(self, predator):
#         print(f"Sentinal bird sees the {predator}")
#         for observer in self.observers:
#             observer.notify_observer(predator)

# sentinal1 = SentinalBird()

# sentinal1.register_observer(BirdObserver("sparrow"))
# sentinal1.register_observer(BirdObserver("finch"))
# sentinal1.register_observer(BirdObserver("robin"))

# sentinal1.spot_predator("hawk")
