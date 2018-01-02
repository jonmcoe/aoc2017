import sys

from shared import get_exact_rows, parse_duet_instruction, DuetMachine


if __name__ == '__main__':
    instructions = [parse_duet_instruction(l) for l in get_exact_rows(sys.argv[1])]
    dm0 = DuetMachine(0, instructions)
    dm1 = DuetMachine(1, instructions)
    dm0.recipient = dm1
    dm1.recipient = dm0

    keep_running = True
    turn = 0
    while keep_running:
        dm0.run_instructions()
        dm1.run_instructions()
        messages_remain = bool(len(dm0.message_queue) + len(dm1.message_queue))
        neither_terminated = not (dm0.terminated or dm1.terminated)
        keep_running = messages_remain and neither_terminated
        turn += 1

    print(dm1.messages_sent)
