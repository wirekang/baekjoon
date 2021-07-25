const regSet = /^{(.*)}$/

;(() => {
	const fs = require("fs")
	const lines = fs.readFileSync("/dev/stdin").toString().split("\n")
	const size = parseInt(lines[0], 10)
	for (let i = 0; i < size; i += 1) {
		const r = isSet(lines[i + 1])
		console.log(`Word #${i + 1}: ${r ? "Set" : "No Set"}`)
	}
})()

function isSet(str) {
	const match = regSet.exec(str)
	return match !== null && isElementList(match[1])
}

function isElementList(str) {
	return isList(str) || str === ""
}

function isList(str) {
	let comma = str
	while (true) {
		if (comma.length === 1) {
			return isAtom(comma)
		}

		if (comma.length > 2 && comma[0] === "," && comma[1] === ",") {
			comma = comma.slice(2)
			continue
		}

		const index = comma.indexOf(",")
		if (index === -1) {
			return isElement(comma)
		}

		const before = comma.slice(0, index)
		comma = comma.slice(index + 1)
		const r = isElement(before) && isList(comma)
		if (r) {
			return true
		}
	}
}

function isElement(str) {
	return isAtom(str) || isSet(str)
}

function isAtom(str) {
	return str === "{" || str === "}" || str === ","
}
