import { sum } from "./my_math"

test("basic", () => {
    expect(sum(-3, 3)).toBe(0)
})

test("basic again", () => {
    expect(sum(1, 2)).toBe(3)
})
