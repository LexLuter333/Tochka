import json


def check_capacity(max_capacity: int, guests: list) -> bool:
    hotel = []
    for guest in guests:
        check_in = guest["check-in"]
        check_out = guest["check-out"]
        hotel.append([check_in, 1])
        hotel.append([check_out, 0])
    hotel.sort(key=lambda check: [check[0], check[1]])

    count = 0

    for guest in hotel:
        if guest[1] == 1:
            count += 1
        else:
            count -= 1
        if count > max_capacity:
            return False
    return True


if __name__ == "__main__":
    max_capacity = int(input())
    n = int(input())


    guests = []
    for _ in range(n):
        guest_json = input()
        guest_data = json.loads(guest_json)
        guests.append(guest_data)


    result = check_capacity(max_capacity, guests)
    print(result)
