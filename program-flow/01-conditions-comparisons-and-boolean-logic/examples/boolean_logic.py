has_ticket = True
venue_open = True
is_blocked = False
denominator = 0

can_enter = has_ticket and venue_open and not is_blocked
needs_attention = not has_ticket or is_blocked
safe_ratio_check = denominator != 0 and 10 / denominator > 2
display_name = "" or "Guest"

print("Can enter:", can_enter)
print("Needs attention:", needs_attention)
print("Safe ratio check:", safe_ratio_check)
print("Display name:", display_name)
