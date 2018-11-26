export function setItem(key, value) {
    const data = localStorage.getItem('ICON_WED_STORAGE')
    const next = data ? { ...JSON.parse(data) } : {}
    if (value) {
        next[key] = value
    }
    localStorage.setItem('ICON_WED_STORAGE', JSON.stringify(next))
}

export function getItem(key) {
    const data = localStorage.getItem('ICON_WED_STORAGE')
    const current = data ? { ...JSON.parse(data) } : {}
    return current[key]
}