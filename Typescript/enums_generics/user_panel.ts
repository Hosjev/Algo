interface iUser {
	name: string
	role: UserRole
}

enum UserRole {
	Administrator = 'admin',
	Developer = 'devel'
}

function loadUser<T>(): T {
	return JSON.parse('{"name": "Wend", "role": "devel"}')
}

const user = loadUser<iUser>()

switch (user.role) {
	case UserRole.Administrator: console.log('User gets full Control Panel'); break
        case UserRole.Developer: console.log('User gets limited Control Panel'); break
}
