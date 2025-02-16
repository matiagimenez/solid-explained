"""
Interface Segregation (ISP) - “Don’t force clients to depend on interfaces they don’t use!” 
"""

from abc import ABC, abstractmethod
class Worker:
    def print_document(self):
        pass

    def scan_document(self):
        pass

    def fax_document(self):
        pass
    
"""
❌ Violations:
- `Worker` class forces all workers to implement methods they may not need (e.g., `scan_document`, `fax_document`).
- A worker who only prints documents must still implement `scan_document` and `fax_document`, which violates ISP.
"""

class PrintWorker(Worker):
    def print_document(self):
        print("Printing document")

    def scan_document(self):
        raise NotImplementedError("This worker doesn't scan.")

    def fax_document(self):
        raise NotImplementedError("This worker doesn't fax.")


"""
✅ Solution (Following ISP):
- Break the large interface into smaller, more specific ones. Each worker will only implement the interfaces relevant to their role.
"""

# Define specific interfaces for each task
class Printer(ABC):
    @abstractmethod
    def print_document(self):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan_document(self):
        pass

class Faxer(ABC):
    @abstractmethod
    def fax_document(self):
        pass


# Workers that only implement the interfaces they need
class PrintWorker(Printer):
    def print_document(self):
        print("Printing document")


class ScanWorker(Scanner):
    def scan_document(self):
        print("Scanning document")


class FaxWorker(Faxer):
    def fax_document(self):
        print("Faxing document")


"""
Now each worker only implements the interfaces they need. This way, they are not forced to implement unnecessary methods.
"""

# Client code: Functions that accept only the specific functionality they need
def perform_printing(worker: Printer):
    worker.print_document()

def perform_scanning(worker: Scanner):
    worker.scan_document()

def perform_faxing(worker: Faxer):
    worker.fax_document()


# Creating workers
printer = PrintWorker()
scanner = ScanWorker()
faxer = FaxWorker()

# Using the workers with the correct interfaces
perform_printing(printer)  # ✅ Works fine
perform_scanning(scanner)  # ✅ Works fine
perform_faxing(faxer)      # ✅ Works fine

# The following would raise errors because the workers don't implement the methods:
# perform_scanning(printer)  # ❌ Not implemented
# perform_faxing(scanner)    # ❌ Not implemented