--
-- Created by IntelliJ IDEA.
-- User: warren
-- Date: 2016/5/3
-- Time: 16:47
-- function: get HAProxy config.
--

function read_config_file(cmdline)
    local found = false
    local filename = ''
    for s in string.gmatch(cmdline, '%g+') do
        if s == '-f' then
            found = true
        elseif found then
            filename = s
            break
        end
    end

    local f = io.open(filename, "rb")
    local config = f:read("*all")
    f:close()
    return config
end

function load_config()
    local f = io.open('/proc/self/cmdline', "rb")
    local cmdline = f:read("*all")
    f:close()
    return read_config_file(cmdline)
end

core.register_init(function()
    haproxy_config = load_config()
end)

core.register_service("getconfig", "http", function(applet)
    applet:set_status(200)
    applet:add_header("content-length", string.len(haproxy_config))
    applet:add_header("content-type", "text/plain")
    applet:start_response()
    applet:send(haproxy_config)
end)
