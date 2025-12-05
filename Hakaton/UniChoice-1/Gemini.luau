local HTTPService = game:GetService("HttpService")

local APIKey = "AIzaSyANn5oeSftBT9qj_CIOjjtqcjITEPCpdX8"
local URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=" .. APIKey

local module = {}

function module.chat(history, instruction)
	local requestbody = {
		system_instruction = {
			parts = {
				text = instruction
			}
		},

		contents = history
	}

	requestbody = HTTPService:JSONEncode(requestbody)

	local requestData = {
		Url = URL,
		Method = "POST",
		Headers = {
			["Content-Type"] = "application/json"
		},
		Body = requestbody
	}

	local success, result = pcall(function()
		return HTTPService:RequestAsync(requestData)
	end)

	if success then
		if result and result.Success then
			local responseData = HTTPService:JSONDecode(result.Body)
			return responseData.candidates[1].content.parts[1].text
		else
			return "Извините произошла ошибка"
		end
	end
end

return module
