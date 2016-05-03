--
-- Created by IntelliJ IDEA.
-- User: warren
-- Date: 2016/5/3
-- Time: 16:47
-- function: get HAProxy pid.
--

function os.capture(cmd)
  local f = assert(io.popen(cmd, 'r'))
  local s = assert(f:read('*a'))
  f:close()
  s = string.gsub(s, '^%s+', '')
  s = string.gsub(s, '%s+$', '')
  s = string.gsub(s, '[\n\r]+', ' ')
  return s
end

core.register_service("getpids", "http", function(applet)
  local response = os.capture("pidof HAProxy", false)
  applet:set_status(200)
  applet:add_header("content-length", string.len(response))
  applet:add_header("content-type", "text/plain")
  applet:start_response()
  applet:send(response)
end)

