import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.review_system import ReviewSystem
from invoker.command_invoker import CommandInvoker
from commands.add_review_command import AddReviewCommand
from commands.edit_review_command import EditReviewCommand
from commands.delete_review_command import DeleteReviewCommand

if __name__ == "__main__":
    system = ReviewSystem()
    invoker = CommandInvoker()

    cmd1 = AddReviewCommand(system, "Daniel Salazar", "Excelente tutor. ⭐⭐⭐⭐⭐")
    cmd2 = AddReviewCommand(system, "Daniel Salazar", "Explica muy claro. ⭐⭐⭐⭐")
    cmd3 = EditReviewCommand(system, "Daniel Salazar", 1, "Muy claro y paciente. ⭐⭐⭐⭐⭐")
    cmd4 = DeleteReviewCommand(system, "Daniel Salazar", 0)

    invoker.run_command(cmd1)
    invoker.run_command(cmd2)
    invoker.run_command(cmd3)
    invoker.run_command(cmd4)
