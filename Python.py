# IndoBeachBot.py - Script Generator Roblox
# Dibuat oleh: Apis
# Versi: 1.0
# Tujuan: Untuk membuat/menghasilkan script Lua secara otomatis (Fly, Invisible, ESP, dll)
# Platform: Replit (Python terminal-based)
# Status: BUKAN untuk injeksi langsung. HANYA untuk generate & simpan script.

"""
📌 INFORMASI PENTING:

1. 🧠 SCRIPT INI BUKAN UNTUK INJECT LANGSUNG
   - Script ini hanya generator teks (Lua), bukan injector.
   - Tidak bisa digunakan langsung di HP untuk Roblox (hanya buat persiapan).

2. 🔐 BUTUH EXECUTOR (PC) UNTUK MENJALANKAN SCRIPT LUA
   - Contoh: KRNL, Synapse X, Fluxus, dll.
   - Load script-nya dari GitHub dengan: 
     loadstring(game:HttpGet("https://raw.githubusercontent.com/..."))()

3. 🗂️ BUTUH GITHUB (atau layanan penyimpanan file .lua RAW)
   - Supaya script hasil dari sini bisa diakses oleh executor.

4. 🗺️ BUTUH ID MAP (PLACE ID) UNTUK AKURASI
   - Contoh: Indo Beach Night Club = 135513289638898
   - Gunakan dalam script Lua seperti:
     if game.PlaceId == 135513289638898 then
         -- jalankan script

5. ⚠️ TANGGUNG JAWAB
   - Script ini disediakan hanya untuk edukasi & koleksi.
   - Penggunaan untuk cheating/exploit adalah risiko pengguna.
   - Developer/script owner tidak bertanggung jawab atas pelanggaran TOS Roblox.

6. 👨‍💻 CONTOH FITUR YANG BISA DIGENERATE:
   - Fly (terbang tekan tombol)
   - Invisible (karakter tembus pandang)
   - Auto Press Key (buat AFK farming)
   - Auto Fishing
   - ESP Money (menampilkan visual posisi uang di map)

7. 💻 CARA PAKAI:
   - Buka Replit.com → Buat project Python
   - Paste script ini ke file IndoBeachBot.py
   - Jalankan script → Pilih fitur → Copy hasil script Lua
   - Upload hasil ke GitHub → Inject di executor PC

"""

import os
import time
import json
from datetime import datetime

class Colors:
    """ANSI Color codes untuk styling terminal"""
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    
    # Colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Bright colors
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    
    # Background colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'

class IndoBeachBot:
    def __init__(self):
        self.version = "1.0"
        self.author = "Apis"
        self.generated_scripts = []
        
    def clear_screen(self):
        """Clear terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def show_button_press(self, button_name):
        """Show animated button press effect"""
        print(f"\n{Colors.BRIGHT_WHITE}┌{'─' * (len(button_name) + 4)}┐{Colors.RESET}")
        print(f"{Colors.BRIGHT_WHITE}│ {Colors.BG_BRIGHT_MAGENTA}{Colors.BRIGHT_WHITE} {button_name} PRESSED! {Colors.RESET}{Colors.BRIGHT_WHITE} │{Colors.RESET}")
        print(f"{Colors.BRIGHT_WHITE}└{'─' * (len(button_name) + 4)}┘{Colors.RESET}")
        time.sleep(0.5)
        
    def print_banner(self):
        """Print stylish banner dengan tema purple"""
        banner = f"""
{Colors.BRIGHT_MAGENTA}╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║  {Colors.BRIGHT_WHITE}███╗   ██╗██████╗  ██████╗     ██████╗ ███████╗ █████╗  ██████╗██╗  ██╗{Colors.BRIGHT_MAGENTA}  ║
║  {Colors.BRIGHT_WHITE}████╗  ██║██╔══██╗██╔═══██╗    ██╔══██╗██╔════╝██╔══██╗██╔════╝██║  ██║{Colors.BRIGHT_MAGENTA}  ║
║  {Colors.BRIGHT_WHITE}██╔██╗ ██║██║  ██║██║   ██║    ██████╔╝█████╗  ███████║██║     ███████║{Colors.BRIGHT_MAGENTA}  ║
║  {Colors.BRIGHT_WHITE}██║╚██╗██║██║  ██║██║   ██║    ██╔══██╗██╔══╝  ██╔══██║██║     ██╔══██║{Colors.BRIGHT_MAGENTA}  ║
║  {Colors.BRIGHT_WHITE}██║ ╚████║██████╔╝╚██████╔╝    ██████╔╝███████╗██║  ██║╚██████╗██║  ██║{Colors.BRIGHT_MAGENTA}  ║
║  {Colors.BRIGHT_WHITE}╚═╝  ╚═══╝╚═════╝  ╚═════╝     ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝{Colors.BRIGHT_MAGENTA}  ║
║                                                                  ║
║                    {Colors.BRIGHT_CYAN}🤖 ROBLOX LUA SCRIPT GENERATOR 🤖{Colors.BRIGHT_MAGENTA}                    ║
║                                                                  ║
║  {Colors.BRIGHT_WHITE}Author:{Colors.BRIGHT_YELLOW} {self.author}                   {Colors.BRIGHT_WHITE}Version:{Colors.BRIGHT_YELLOW} {self.version}{Colors.BRIGHT_MAGENTA}                        ║
║  {Colors.BRIGHT_WHITE}Platform:{Colors.BRIGHT_GREEN} Replit Python          {Colors.BRIGHT_WHITE}Status:{Colors.BRIGHT_RED} Generator Only{Colors.BRIGHT_MAGENTA}        ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝{Colors.RESET}
"""
        print(banner)
        
    def print_menu(self):
        """Print main menu dengan styling tombol yang bagus"""
        menu = f"""
{Colors.BRIGHT_MAGENTA}╔═══════════════════════════════════════════════════════════════════╗
║                         {Colors.BRIGHT_WHITE}🎮 SCRIPT GENERATOR MENU 🎮{Colors.BRIGHT_MAGENTA}                        ║
╠═══════════════════════════════════════════════════════════════════╣
║                                                                   ║
║   {Colors.BG_MAGENTA}{Colors.BRIGHT_WHITE} [1] 🚁 FLY SCRIPT {Colors.RESET}{Colors.BRIGHT_MAGENTA}        {Colors.BG_BLUE}{Colors.BRIGHT_WHITE} [6] 🎣 AUTO FISHING {Colors.RESET}{Colors.BRIGHT_MAGENTA}   ║
║   {Colors.BRIGHT_CYAN}▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔{Colors.BRIGHT_MAGENTA}        {Colors.BRIGHT_CYAN}▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔{Colors.BRIGHT_MAGENTA}   ║
║                                                                   ║
║   {Colors.BG_MAGENTA}{Colors.BRIGHT_WHITE} [2] 👻 INVISIBLE {Colors.RESET}{Colors.BRIGHT_MAGENTA}           {Colors.BG_BLUE}{Colors.BRIGHT_WHITE} [7] 💰 ESP MONEY {Colors.RESET}{Colors.BRIGHT_MAGENTA}      ║
║   {Colors.BRIGHT_CYAN}▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔{Colors.BRIGHT_MAGENTA}        {Colors.BRIGHT_CYAN}▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔{Colors.BRIGHT_MAGENTA}   ║
║                                                                   ║
║   {Colors.BG_MAGENTA}{Colors.BRIGHT_WHITE} [3] ⚡ SPEED BOOST {Colors.RESET}{Colors.BRIGHT_MAGENTA}         {Colors.BG_BLUE}{Colors.BRIGHT_WHITE} [8] 🔧 CUSTOM SCRIPT {Colors.RESET}{Colors.BRIGHT_MAGENTA} ║
║   {Colors.BRIGHT_CYAN}▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔{Colors.BRIGHT_MAGENTA}        {Colors.BRIGHT_CYAN}▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔{Colors.BRIGHT_MAGENTA}   ║
║                                                                   ║
║   {Colors.BG_MAGENTA}{Colors.BRIGHT_WHITE} [4] 🎯 AUTO KEY PRESS {Colors.RESET}{Colors.BRIGHT_MAGENTA}     {Colors.BG_BLUE}{Colors.BRIGHT_WHITE} [9] 📝 VIEW SCRIPTS {Colors.RESET}{Colors.BRIGHT_MAGENTA}  ║
║   {Colors.BRIGHT_CYAN}▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔{Colors.BRIGHT_MAGENTA}       {Colors.BRIGHT_CYAN}▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔{Colors.BRIGHT_MAGENTA}   ║
║                                                                   ║
║   {Colors.BG_MAGENTA}{Colors.BRIGHT_WHITE} [5] 🏃 NO CLIP {Colors.RESET}{Colors.BRIGHT_MAGENTA}                                              ║
║   {Colors.BRIGHT_CYAN}▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔{Colors.BRIGHT_MAGENTA}                                               ║
║                                                                   ║
║                    {Colors.BG_RED}{Colors.BRIGHT_WHITE} [0] ❌ EXIT PROGRAM {Colors.RESET}{Colors.BRIGHT_MAGENTA}                      ║
║                    {Colors.BRIGHT_RED}▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔{Colors.BRIGHT_MAGENTA}                      ║
║                                                                   ║
╠═══════════════════════════════════════════════════════════════════╣
║  {Colors.BRIGHT_YELLOW}💡 Tip: Klik nomor tombol untuk generate script Lua otomatis!{Colors.BRIGHT_MAGENTA}     ║
║  {Colors.BRIGHT_GREEN}🚀 Generated scripts akan disimpan sebagai file .lua{Colors.BRIGHT_MAGENTA}              ║
╚═══════════════════════════════════════════════════════════════════╝{Colors.RESET}
"""
        print(menu)
        
    def generate_fly_script(self):
        """Generate Fly script"""
        place_id = input(f"{Colors.BRIGHT_YELLOW}Enter Place ID (default: 135513289638898): {Colors.RESET}") or "135513289638898"
        key_bind = input(f"{Colors.BRIGHT_YELLOW}Fly key (default: F): {Colors.RESET}") or "F"
        
        script = f'''-- 🚁 Fly Script for Roblox
-- Generated by IndoBeachBot v{self.version}
-- Author: {self.author}
-- Date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

-- Place ID Check
if game.PlaceId ~= {place_id} then
    game.Players.LocalPlayer:Kick("❌ Script ini hanya untuk Indo Beach Night Club!")
    return
end

local Players = game:GetService("Players")
local UserInputService = game:GetService("UserInputService")
local RunService = game:GetService("RunService")

local player = Players.LocalPlayer
local character = player.Character or player.CharacterAdded:Wait()
local humanoid = character:WaitForChild("Humanoid")
local rootPart = character:WaitForChild("HumanoidRootPart")

local flying = false
local speed = 50
local bodyVelocity

-- Create GUI
local screenGui = Instance.new("ScreenGui")
screenGui.Name = "FlyGUI"
screenGui.Parent = player:WaitForChild("PlayerGui")

local frame = Instance.new("Frame")
frame.Size = UDim2.new(0, 200, 0, 100)
frame.Position = UDim2.new(0, 10, 0, 10)
frame.BackgroundColor3 = Color3.new(0.1, 0.1, 0.1)
frame.BorderSizePixel = 0
frame.Parent = screenGui

local title = Instance.new("TextLabel")
title.Size = UDim2.new(1, 0, 0, 30)
title.Position = UDim2.new(0, 0, 0, 0)
title.BackgroundColor3 = Color3.new(0.2, 0, 0.4)
title.TextColor3 = Color3.new(1, 1, 1)
title.Text = "🚁 Fly Script"
title.TextScaled = true
title.Font = Enum.Font.GothamBold
title.Parent = frame

local statusLabel = Instance.new("TextLabel")
statusLabel.Size = UDim2.new(1, 0, 0, 30)
statusLabel.Position = UDim2.new(0, 0, 0, 35)
statusLabel.BackgroundTransparency = 1
statusLabel.TextColor3 = Color3.new(1, 1, 1)
statusLabel.Text = "Press {key_bind} to toggle fly"
statusLabel.TextScaled = true
statusLabel.Font = Enum.Font.Gotham
statusLabel.Parent = frame

local speedLabel = Instance.new("TextLabel")
speedLabel.Size = UDim2.new(1, 0, 0, 30)
speedLabel.Position = UDim2.new(0, 0, 0, 65)
speedLabel.BackgroundTransparency = 1
speedLabel.TextColor3 = Color3.new(0.8, 0.8, 0.8)
speedLabel.Text = "Speed: " .. speed
speedLabel.TextScaled = true
speedLabel.Font = Enum.Font.Gotham
speedLabel.Parent = frame

-- Fly function
local function toggleFly()
    flying = not flying
    
    if flying then
        -- Start flying
        bodyVelocity = Instance.new("BodyVelocity")
        bodyVelocity.MaxForce = Vector3.new(4000, 4000, 4000)
        bodyVelocity.Velocity = Vector3.new(0, 0, 0)
        bodyVelocity.Parent = rootPart
        
        humanoid.PlatformStand = true
        statusLabel.Text = "✅ Flying Active"
        statusLabel.TextColor3 = Color3.new(0, 1, 0)
        
        -- Flying loop
        RunService.Heartbeat:Connect(function()
            if flying and bodyVelocity then
                local camera = workspace.CurrentCamera
                local moveVector = humanoid.MoveDirection * speed
                
                bodyVelocity.Velocity = Vector3.new(
                    moveVector.X,
                    0,
                    moveVector.Z
                )
                
                -- Handle up/down movement
                if UserInputService:IsKeyDown(Enum.KeyCode.Space) then
                    bodyVelocity.Velocity = bodyVelocity.Velocity + Vector3.new(0, speed, 0)
                elseif UserInputService:IsKeyDown(Enum.KeyCode.LeftShift) then
                    bodyVelocity.Velocity = bodyVelocity.Velocity + Vector3.new(0, -speed, 0)
                end
            end
        end)
    else
        -- Stop flying
        if bodyVelocity then
            bodyVelocity:Destroy()
            bodyVelocity = nil
        end
        
        humanoid.PlatformStand = false
        statusLabel.Text = "❌ Flying Disabled"
        statusLabel.TextColor3 = Color3.new(1, 0, 0)
    end
end

-- Key binding
UserInputService.InputBegan:Connect(function(input, gameProcessed)
    if gameProcessed then return end
    
    if input.KeyCode == Enum.KeyCode.{key_bind} then
        toggleFly()
    elseif input.KeyCode == Enum.KeyCode.Equal then
        speed = math.min(speed + 10, 200)
        speedLabel.Text = "Speed: " .. speed
    elseif input.KeyCode == Enum.KeyCode.Minus then
        speed = math.max(speed - 10, 10)
        speedLabel.Text = "Speed: " .. speed
    end
end)

-- Character respawn handling
player.CharacterAdded:Connect(function(newCharacter)
    character = newCharacter
    humanoid = character:WaitForChild("Humanoid")
    rootPart = character:WaitForChild("HumanoidRootPart")
    flying = false
    statusLabel.Text = "Press {key_bind} to toggle fly"
    statusLabel.TextColor3 = Color3.new(1, 1, 1)
end)

print("🚁 Fly Script loaded! Press {key_bind} to toggle, +/- to change speed")'''

        return script
    
    def generate_invisible_script(self):
        """Generate Invisible script"""
        place_id = input(f"{Colors.BRIGHT_YELLOW}Enter Place ID (default: 135513289638898): {Colors.RESET}") or "135513289638898"
        key_bind = input(f"{Colors.BRIGHT_YELLOW}Invisible key (default: G): {Colors.RESET}") or "G"
        
        script = f'''-- 👻 Invisible Script for Roblox
-- Generated by IndoBeachBot v{self.version}
-- Author: {self.author}
-- Date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

-- Place ID Check
if game.PlaceId ~= {place_id} then
    game.Players.LocalPlayer:Kick("❌ Script ini hanya untuk Indo Beach Night Club!")
    return
end

local Players = game:GetService("Players")
local UserInputService = game:GetService("UserInputService")
local RunService = game:GetService("RunService")

local player = Players.LocalPlayer
local character = player.Character or player.CharacterAdded:Wait()
local invisible = false

-- Create GUI
local screenGui = Instance.new("ScreenGui")
screenGui.Name = "InvisibleGUI"
screenGui.Parent = player:WaitForChild("PlayerGui")

local frame = Instance.new("Frame")
frame.Size = UDim2.new(0, 200, 0, 80)
frame.Position = UDim2.new(0, 10, 0, 120)
frame.BackgroundColor3 = Color3.new(0.1, 0.1, 0.1)
frame.BorderSizePixel = 0
frame.Parent = screenGui

local title = Instance.new("TextLabel")
title.Size = UDim2.new(1, 0, 0, 30)
title.Position = UDim2.new(0, 0, 0, 0)
title.BackgroundColor3 = Color3.new(0.4, 0, 0.2)
title.TextColor3 = Color3.new(1, 1, 1)
title.Text = "👻 Invisible Script"
title.TextScaled = true
title.Font = Enum.Font.GothamBold
title.Parent = frame

local statusLabel = Instance.new("TextLabel")
statusLabel.Size = UDim2.new(1, 0, 0, 45)
statusLabel.Position = UDim2.new(0, 0, 0, 35)
statusLabel.BackgroundTransparency = 1
statusLabel.TextColor3 = Color3.new(1, 1, 1)
statusLabel.Text = "Press {key_bind} to toggle invisible"
statusLabel.TextScaled = true
statusLabel.Font = Enum.Font.Gotham
statusLabel.Parent = frame

-- Store original transparency values
local originalTransparency = {{}}

local function saveOriginalTransparency()
    originalTransparency = {{}}
    for _, part in pairs(character:GetChildren()) do
        if part:IsA("BasePart") and part.Name ~= "HumanoidRootPart" then
            originalTransparency[part] = part.Transparency
        elseif part:IsA("Accessory") then
            for _, accessoryPart in pairs(part:GetChildren()) do
                if accessoryPart:IsA("BasePart") then
                    originalTransparency[accessoryPart] = accessoryPart.Transparency
                end
            end
        end
    end
end

local function toggleInvisible()
    invisible = not invisible
    
    if invisible then
        -- Make invisible
        saveOriginalTransparency()
        
        for _, part in pairs(character:GetChildren()) do
            if part:IsA("BasePart") and part.Name ~= "HumanoidRootPart" then
                part.Transparency = 1
                if part:FindFirstChild("face") then
                    part.face.Transparency = 1
                end
            elseif part:IsA("Accessory") then
                for _, accessoryPart in pairs(part:GetChildren()) do
                    if accessoryPart:IsA("BasePart") then
                        accessoryPart.Transparency = 1
                    end
                end
            end
        end
        
        statusLabel.Text = "✅ Invisible Active"
        statusLabel.TextColor3 = Color3.new(0, 1, 0)
    else
        -- Make visible
        for part, transparency in pairs(originalTransparency) do
            if part and part.Parent then
                part.Transparency = transparency
                if part:FindFirstChild("face") then
                    part.face.Transparency = 0
                end
            end
        end
        
        statusLabel.Text = "❌ Invisible Disabled"
        statusLabel.TextColor3 = Color3.new(1, 0, 0)
    end
end

-- Key binding
UserInputService.InputBegan:Connect(function(input, gameProcessed)
    if gameProcessed then return end
    
    if input.KeyCode == Enum.KeyCode.{key_bind} then
        toggleInvisible()
    end
end)

-- Character respawn handling
player.CharacterAdded:Connect(function(newCharacter)
    character = newCharacter
    invisible = false
    originalTransparency = {{}}
    statusLabel.Text = "Press {key_bind} to toggle invisible"
    statusLabel.TextColor3 = Color3.new(1, 1, 1)
end)

print("👻 Invisible Script loaded! Press {key_bind} to toggle")'''

        return script
    
    def generate_speed_script(self):
        """Generate Speed Boost script"""
        place_id = input(f"{Colors.BRIGHT_YELLOW}Enter Place ID (default: 135513289638898): {Colors.RESET}") or "135513289638898"
        speed_value = input(f"{Colors.BRIGHT_YELLOW}Speed multiplier (default: 50): {Colors.RESET}") or "50"
        
        script = f'''-- ⚡ Speed Boost Script for Roblox
-- Generated by IndoBeachBot v{self.version}
-- Author: {self.author}
-- Date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

-- Place ID Check
if game.PlaceId ~= {place_id} then
    game.Players.LocalPlayer:Kick("❌ Script ini hanya untuk Indo Beach Night Club!")
    return
end

local Players = game:GetService("Players")
local UserInputService = game:GetService("UserInputService")

local player = Players.LocalPlayer
local character = player.Character or player.CharacterAdded:Wait()
local humanoid = character:WaitForChild("Humanoid")

local originalSpeed = humanoid.WalkSpeed
local speedMultiplier = {speed_value}
local speedEnabled = false

-- Create GUI
local screenGui = Instance.new("ScreenGui")
screenGui.Name = "SpeedGUI"
screenGui.Parent = player:WaitForChild("PlayerGui")

local frame = Instance.new("Frame")
frame.Size = UDim2.new(0, 200, 0, 100)
frame.Position = UDim2.new(0, 10, 0, 210)
frame.BackgroundColor3 = Color3.new(0.1, 0.1, 0.1)
frame.BorderSizePixel = 0
frame.Parent = screenGui

local title = Instance.new("TextLabel")
title.Size = UDim2.new(1, 0, 0, 30)
title.Position = UDim2.new(0, 0, 0, 0)
title.BackgroundColor3 = Color3.new(0.2, 0.4, 0)
title.TextColor3 = Color3.new(1, 1, 1)
title.Text = "⚡ Speed Boost"
title.TextScaled = true
title.Font = Enum.Font.GothamBold
title.Parent = frame

local statusLabel = Instance.new("TextLabel")
statusLabel.Size = UDim2.new(1, 0, 0, 30)
statusLabel.Position = UDim2.new(0, 0, 0, 35)
statusLabel.BackgroundTransparency = 1
statusLabel.TextColor3 = Color3.new(1, 1, 1)
statusLabel.Text = "Press H to toggle speed"
statusLabel.TextScaled = true
statusLabel.Font = Enum.Font.Gotham
statusLabel.Parent = frame

local speedLabel = Instance.new("TextLabel")
speedLabel.Size = UDim2.new(1, 0, 0, 30)
speedLabel.Position = UDim2.new(0, 0, 0, 65)
speedLabel.BackgroundTransparency = 1
speedLabel.TextColor3 = Color3.new(0.8, 0.8, 0.8)
speedLabel.Text = "Current: " .. humanoid.WalkSpeed
speedLabel.TextScaled = true
speedLabel.Font = Enum.Font.Gotham
speedLabel.Parent = frame

local function toggleSpeed()
    speedEnabled = not speedEnabled
    
    if speedEnabled then
        humanoid.WalkSpeed = speedMultiplier
        statusLabel.Text = "✅ Speed Boost Active"
        statusLabel.TextColor3 = Color3.new(0, 1, 0)
    else
        humanoid.WalkSpeed = originalSpeed
        statusLabel.Text = "❌ Speed Boost Disabled"
        statusLabel.TextColor3 = Color3.new(1, 0, 0)
    end
    
    speedLabel.Text = "Current: " .. humanoid.WalkSpeed
end

-- Key binding
UserInputService.InputBegan:Connect(function(input, gameProcessed)
    if gameProcessed then return end
    
    if input.KeyCode == Enum.KeyCode.H then
        toggleSpeed()
    elseif input.KeyCode == Enum.KeyCode.Equal then
        speedMultiplier = math.min(speedMultiplier + 10, 500)
        if speedEnabled then
            humanoid.WalkSpeed = speedMultiplier
            speedLabel.Text = "Current: " .. humanoid.WalkSpeed
        end
    elseif input.KeyCode == Enum.KeyCode.Minus then
        speedMultiplier = math.max(speedMultiplier - 10, 16)
        if speedEnabled then
            humanoid.WalkSpeed = speedMultiplier
            speedLabel.Text = "Current: " .. humanoid.WalkSpeed
        end
    end
end)

-- Character respawn handling
player.CharacterAdded:Connect(function(newCharacter)
    character = newCharacter
    humanoid = character:WaitForChild("Humanoid")
    originalSpeed = humanoid.WalkSpeed
    speedEnabled = false
    statusLabel.Text = "Press H to toggle speed"
    statusLabel.TextColor3 = Color3.new(1, 1, 1)
    speedLabel.Text = "Current: " .. humanoid.WalkSpeed
end)

print("⚡ Speed Boost Script loaded! Press H to toggle, +/- to adjust speed")'''

        return script
    
    def generate_auto_key_script(self):
        """Generate Auto Press Key script"""
        place_id = input(f"{Colors.BRIGHT_YELLOW}Enter Place ID (default: 135513289638898): {Colors.RESET}") or "135513289638898"
        target_key = input(f"{Colors.BRIGHT_YELLOW}Key to auto-press (default: E): {Colors.RESET}") or "E"
        interval = input(f"{Colors.BRIGHT_YELLOW}Interval in seconds (default: 1): {Colors.RESET}") or "1"
        
        script = f'''-- 🎯 Auto Press Key Script for Roblox
-- Generated by IndoBeachBot v{self.version}
-- Author: {self.author}
-- Date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

-- Place ID Check
if game.PlaceId ~= {place_id} then
    game.Players.LocalPlayer:Kick("❌ Script ini hanya untuk Indo Beach Night Club!")
    return
end

local Players = game:GetService("Players")
local UserInputService = game:GetService("UserInputService")
local VirtualInputManager = game:GetService("VirtualInputManager")
local RunService = game:GetService("RunService")

local player = Players.LocalPlayer
local autoPress = false
local interval = {interval}
local lastPress = 0

-- Create GUI
local screenGui = Instance.new("ScreenGui")
screenGui.Name = "AutoKeyGUI"
screenGui.Parent = player:WaitForChild("PlayerGui")

local frame = Instance.new("Frame")
frame.Size = UDim2.new(0, 200, 0, 120)
frame.Position = UDim2.new(0, 10, 0, 320)
frame.BackgroundColor3 = Color3.new(0.1, 0.1, 0.1)
frame.BorderSizePixel = 0
frame.Parent = screenGui

local title = Instance.new("TextLabel")
title.Size = UDim2.new(1, 0, 0, 30)
title.Position = UDim2.new(0, 0, 0, 0)
title.BackgroundColor3 = Color3.new(0, 0.2, 0.4)
title.TextColor3 = Color3.new(1, 1, 1)
title.Text = "🎯 Auto Key Press"
title.TextScaled = true
title.Font = Enum.Font.GothamBold
title.Parent = frame

local statusLabel = Instance.new("TextLabel")
statusLabel.Size = UDim2.new(1, 0, 0, 30)
statusLabel.Position = UDim2.new(0, 0, 0, 35)
statusLabel.BackgroundTransparency = 1
statusLabel.TextColor3 = Color3.new(1, 1, 1)
statusLabel.Text = "Press J to toggle auto press"
statusLabel.TextScaled = true
statusLabel.Font = Enum.Font.Gotham
statusLabel.Parent = frame

local keyLabel = Instance.new("TextLabel")
keyLabel.Size = UDim2.new(1, 0, 0, 25)
keyLabel.Position = UDim2.new(0, 0, 0, 65)
keyLabel.BackgroundTransparency = 1
keyLabel.TextColor3 = Color3.new(0.8, 0.8, 0.8)
keyLabel.Text = "Target Key: {target_key}"
keyLabel.TextScaled = true
keyLabel.Font = Enum.Font.Gotham
keyLabel.Parent = frame

local intervalLabel = Instance.new("TextLabel")
intervalLabel.Size = UDim2.new(1, 0, 0, 25)
intervalLabel.Position = UDim2.new(0, 0, 0, 90)
intervalLabel.BackgroundTransparency = 1
intervalLabel.TextColor3 = Color3.new(0.8, 0.8, 0.8)
intervalLabel.Text = "Interval: " .. interval .. "s"
intervalLabel.TextScaled = true
intervalLabel.Font = Enum.Font.Gotham
intervalLabel.Parent = frame

local function toggleAutoPress()
    autoPress = not autoPress
    
    if autoPress then
        statusLabel.Text = "✅ Auto Press Active"
        statusLabel.TextColor3 = Color3.new(0, 1, 0)
        lastPress = tick()
    else
        statusLabel.Text = "❌ Auto Press Disabled"
        statusLabel.TextColor3 = Color3.new(1, 0, 0)
    end
end

-- Auto press loop
RunService.Heartbeat:Connect(function()
    if autoPress and tick() - lastPress >= interval then
        -- Simulate key press
        VirtualInputManager:SendKeyEvent(true, Enum.KeyCode.{target_key}, false, game)
        wait(0.1)
        VirtualInputManager:SendKeyEvent(false, Enum.KeyCode.{target_key}, false, game)
        lastPress = tick()
    end
end)

-- Key binding
UserInputService.InputBegan:Connect(function(input, gameProcessed)
    if gameProcessed then return end
    
    if input.KeyCode == Enum.KeyCode.J then
        toggleAutoPress()
    elseif input.KeyCode == Enum.KeyCode.Equal then
        interval = math.min(interval + 0.5, 10)
        intervalLabel.Text = "Interval: " .. interval .. "s"
    elseif input.KeyCode == Enum.KeyCode.Minus then
        interval = math.max(interval - 0.5, 0.1)
        intervalLabel.Text = "Interval: " .. interval .. "s"
    end
end)

print("🎯 Auto Key Press Script loaded! Press J to toggle, +/- to adjust interval")'''

        return script
    
    def generate_noclip_script(self):
        """Generate No Clip script"""
        place_id = input(f"{Colors.BRIGHT_YELLOW}Enter Place ID (default: 135513289638898): {Colors.RESET}") or "135513289638898"
        key_bind = input(f"{Colors.BRIGHT_YELLOW}NoClip key (default: N): {Colors.RESET}") or "N"
        
        script = f'''-- 🏃 No Clip Script for Roblox
-- Generated by IndoBeachBot v{self.version}
-- Author: {self.author}
-- Date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

-- Place ID Check
if game.PlaceId ~= {place_id} then
    game.Players.LocalPlayer:Kick("❌ Script ini hanya untuk Indo Beach Night Club!")
    return
end

local Players = game:GetService("Players")
local UserInputService = game:GetService("UserInputService")
local RunService = game:GetService("RunService")

local player = Players.LocalPlayer
local character = player.Character or player.CharacterAdded:Wait()
local noclip = false
local connection

-- Create GUI
local screenGui = Instance.new("ScreenGui")
screenGui.Name = "NoClipGUI"
screenGui.Parent = player:WaitForChild("PlayerGui")

local frame = Instance.new("Frame")
frame.Size = UDim2.new(0, 200, 0, 80)
frame.Position = UDim2.new(0, 10, 0, 450)
frame.BackgroundColor3 = Color3.new(0.1, 0.1, 0.1)
frame.BorderSizePixel = 0
frame.Parent = screenGui

local title = Instance.new("TextLabel")
title.Size = UDim2.new(1, 0, 0, 30)
title.Position = UDim2.new(0, 0, 0, 0)
title.BackgroundColor3 = Color3.new(0.4, 0.2, 0)
title.TextColor3 = Color3.new(1, 1, 1)
title.Text = "🏃 No Clip"
title.TextScaled = true
title.Font = Enum.Font.GothamBold
title.Parent = frame

local statusLabel = Instance.new("TextLabel")
statusLabel.Size = UDim2.new(1, 0, 0, 45)
statusLabel.Position = UDim2.new(0, 0, 0, 35)
statusLabel.BackgroundTransparency = 1
statusLabel.TextColor3 = Color3.new(1, 1, 1)
statusLabel.Text = "Press {key_bind} to toggle noclip"
statusLabel.TextScaled = true
statusLabel.Font = Enum.Font.Gotham
statusLabel.Parent = frame

local function noclipLoop()
    if character then
        for _, part in pairs(character:GetChildren()) do
            if part:IsA("BasePart") and part.CanCollide then
                part.CanCollide = false
            end
        end
    end
end

local function toggleNoclip()
    noclip = not noclip
    
    if noclip then
        -- Enable noclip
        connection = RunService.Stepped:Connect(noclipLoop)
        statusLabel.Text = "✅ No Clip Active"
        statusLabel.TextColor3 = Color3.new(0, 1, 0)
    else
        -- Disable noclip
        if connection then
            connection:Disconnect()
            connection = nil
        end
        
        -- Restore collision
        if character then
            for _, part in pairs(character:GetChildren()) do
                if part:IsA("BasePart") and part.Name ~= "HumanoidRootPart" then
                    part.CanCollide = true
                end
            end
        end
        
        statusLabel.Text = "❌ No Clip Disabled"
        statusLabel.TextColor3 = Color3.new(1, 0, 0)
    end
end

-- Key binding
UserInputService.InputBegan:Connect(function(input, gameProcessed)
    if gameProcessed then return end
    
    if input.KeyCode == Enum.KeyCode.{key_bind} then
        toggleNoclip()
    end
end)

-- Character respawn handling
player.CharacterAdded:Connect(function(newCharacter)
    character = newCharacter
    noclip = false
    if connection then
        connection:Disconnect()
        connection = nil
    end
    statusLabel.Text = "Press {key_bind} to toggle noclip"
    statusLabel.TextColor3 = Color3.new(1, 1, 1)
end)

print("🏃 No Clip Script loaded! Press {key_bind} to toggle")'''

        return script
    
    def save_script(self, script_content, script_name):
        """Save generated script to file"""
        try:
            filename = f"{script_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.lua"
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(script_content)
            
            script_info = {
                'name': script_name,
                'filename': filename,
                'generated_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'size': len(script_content)
            }
            
            self.generated_scripts.append(script_info)
            
            print(f"\n{Colors.BRIGHT_GREEN}✅ Script saved as: {filename}{Colors.RESET}")
            print(f"{Colors.BRIGHT_CYAN}📁 File size: {len(script_content)} characters{Colors.RESET}")
            print(f"{Colors.BRIGHT_YELLOW}💡 Upload this file to GitHub for raw access{Colors.RESET}")
            
            return filename
        except Exception as e:
            print(f"\n{Colors.BRIGHT_RED}❌ Error saving script: {e}{Colors.RESET}")
            return None
    
    def view_generated_scripts(self):
        """View list of generated scripts"""
        if not self.generated_scripts:
            print(f"\n{Colors.BRIGHT_YELLOW}📝 No scripts generated yet.{Colors.RESET}")
            return
        
        print(f"\n{Colors.BRIGHT_CYAN}📋 Generated Scripts History:{Colors.RESET}")
        print(f"{Colors.BRIGHT_MAGENTA}{'='*60}{Colors.RESET}")
        
        for i, script in enumerate(self.generated_scripts, 1):
            print(f"{Colors.BRIGHT_WHITE}[{i}] {script['name']}{Colors.RESET}")
            print(f"    {Colors.BRIGHT_GREEN}📄 File: {script['filename']}{Colors.RESET}")
            print(f"    {Colors.BRIGHT_YELLOW}📅 Generated: {script['generated_at']}{Colors.RESET}")
            print(f"    {Colors.BRIGHT_CYAN}📊 Size: {script['size']} chars{Colors.RESET}")
            print()
    
    def handle_choice(self, choice):
        """Handle menu choice selection"""
        if choice == "1":
            print(f"\n{Colors.BRIGHT_CYAN}🚁 Generating Fly Script...{Colors.RESET}")
            script = self.generate_fly_script()
            filename = self.save_script(script, "FlyScript")
            if filename:
                print(f"\n{Colors.BRIGHT_GREEN}✨ Fly script generated successfully!{Colors.RESET}")
        
        elif choice == "2":
            print(f"\n{Colors.BRIGHT_CYAN}👻 Generating Invisible Script...{Colors.RESET}")
            script = self.generate_invisible_script()
            filename = self.save_script(script, "InvisibleScript")
            if filename:
                print(f"\n{Colors.BRIGHT_GREEN}✨ Invisible script generated successfully!{Colors.RESET}")
        
        elif choice == "3":
            print(f"\n{Colors.BRIGHT_CYAN}⚡ Generating Speed Boost Script...{Colors.RESET}")
            script = self.generate_speed_script()
            filename = self.save_script(script, "SpeedScript")
            if filename:
                print(f"\n{Colors.BRIGHT_GREEN}✨ Speed script generated successfully!{Colors.RESET}")
        
        elif choice == "4":
            print(f"\n{Colors.BRIGHT_CYAN}🎯 Generating Auto Press Key Script...{Colors.RESET}")
            script = self.generate_auto_key_script()
            filename = self.save_script(script, "AutoKeyScript")
            if filename:
                print(f"\n{Colors.BRIGHT_GREEN}✨ Auto Key script generated successfully!{Colors.RESET}")
        
        elif choice == "5":
            print(f"\n{Colors.BRIGHT_CYAN}🏃 Generating No Clip Script...{Colors.RESET}")
            script = self.generate_noclip_script()
            filename = self.save_script(script, "NoClipScript")
            if filename:
                print(f"\n{Colors.BRIGHT_GREEN}✨ No Clip script generated successfully!{Colors.RESET}")
        
        elif choice == "6":
            print(f"\n{Colors.BRIGHT_YELLOW}🎣 Auto Fishing feature coming soon!{Colors.RESET}")
            print(f"{Colors.BRIGHT_CYAN}🔜 Feature ini akan ditambahkan di update berikutnya!{Colors.RESET}")
        
        elif choice == "7":
            print(f"\n{Colors.BRIGHT_YELLOW}💰 ESP Money feature coming soon!{Colors.RESET}")
            print(f"{Colors.BRIGHT_CYAN}🔜 Feature ini akan ditambahkan di update berikutnya!{Colors.RESET}")
        
        elif choice == "8":
            print(f"\n{Colors.BRIGHT_YELLOW}🔧 Custom Script builder coming soon!{Colors.RESET}")
            print(f"{Colors.BRIGHT_CYAN}🔜 Feature ini akan ditambahkan di update berikutnya!{Colors.RESET}")
        
        elif choice == "9":
            self.view_generated_scripts()
        
        else:
            print(f"\n{Colors.BRIGHT_RED}❌ Invalid choice! Please select 0-9.{Colors.RESET}")

    def run(self):
        """Main program loop"""
        self.clear_screen()
        self.print_banner()
        while True:
            self.print_menu()
            choice = input(f"\n{Colors.BRIGHT_CYAN}Masukkan pilihan: {Colors.RESET}")
            if choice == "0":
                print(f"{Colors.BRIGHT_RED}Keluar dari IndoBeachBot...{Colors.RESET}")
                break
            else:
                self.show_button_press(f"Menu {choice}")
                self.handle_choice(choice)
                input(f"\n{Colors.BRIGHT_WHITE}Tekan Enter untuk kembali ke menu...{Colors.RESET}")
                self.clear_screen()
                self.print_banner()

# Main execution
if __name__ == "__main__":
    bot = IndoBeachBot()
    bot.run()