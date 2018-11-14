
use securitydb;

// users: id/firstname/lastname/email/phonenumber/profession

//BSON - Binary JSON
// https://stackoverflow.com/questions/12438280/what-is-bson-and-exactly-how-is-it-different-from-json

db.createCollection("users", {
	validator: {
		$jsonSchema: {
			bsonType: "object",
			required: ["firstname", "lastname", "email", "password"],
			properties: {
				firstname: {
					bsonType: "string"
				},
				lastname: {
					bsonType: "string"
				},
				email: {
					bsonType: "string"
				},
				phonenumber: {
					bsonType: "string"
				},
				password: {
					bsonType: "string"
				},
				registerdate: {
					bsonType: "date"
				},
				role: {
					bsonType: "string"
				}
			}
		}
	}
})

db.createCollection("roles", {
	validator: {
		$jsonSchema: {
			bsonType: "object",
			required: ["role"],
			properties: {
				role: {
					bsonType: "string"
				},
				permissions: {
					bsonType: "array"
				}
			}
		}
	}
})


db.createCollection("permissions", {
	validator: {
		$jsonSchema: {
			bsonType: "object",
			required: ["permission"],
			properties: {
				permission: {
					bsonType: "string"
				}
			}
		}
	}
})

