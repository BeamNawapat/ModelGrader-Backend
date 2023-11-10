import subprocess

def forgiveableFormat(string:str)->str:
    return string.replace('\r','')
    # return string

def checker(section:int,code:str,testcases:list,timeout=1.5)->dict:
    result = []
    hasError = False
    hasTimeout = False
    for i in range(len(testcases)):
        with open(f'./api/sandbox/section{section}/testcases/{i}.txt','w') as f:
            f.write(testcases[i])
    
    with open(f'./api/sandbox/section{section}/runner.py','w') as f:
        f.write(code)

    for i in range(len(testcases)):
        try:
            runner = subprocess.check_output(['python',f'./api/sandbox/section{section}/runner.py'],stdin=open(f'./api/sandbox/section{section}/testcases/{i}.txt','r'),stderr=subprocess.DEVNULL,timeout=float(timeout))
            result.append({'input':testcases[i],'output':runner.decode(),'runtime_status':'OK'})
        except subprocess.CalledProcessError:
            hasError = True
            result.append({'input':testcases[i],'output':None,'runtime_status':'ERROR'})
        except subprocess.TimeoutExpired:
            hasTimeout = True
            result.append({'input':testcases[i],'output':None,'runtime_status':'TIMEOUT'})

    return {'result':result,'has_error':hasError,'has_timeout':hasTimeout}
    
def grading(section:int,code:str,input:list,output:list,timeout=1.5)->str:
    score = ''
    graded = checker(section,code,input,timeout)
    graded_result = graded['result']

    for i in range(len(output)):
        if graded_result[i]['runtime_status'] == 'OK':
            if forgiveableFormat(graded_result[i]['output']) == forgiveableFormat(output[i]):
                score += 'P'
            else:
                score += '-'
        elif graded_result[i]['runtime_status'] == 'TIMEOUT':
            score += 'T'
        else:
            score += 'E'
    
    return score


class RuntimeResult:

    RUNTIME_STATUS = [
        'OK',
        'ERROR',
        'TIMEOUT'
    ]

    def __init__(self,input:str,output:str,runtime_status:RUNTIME_STATUS) -> None:
        self.input = input
        self.output = output
        self.runtime_status = runtime_status

class ProgramGrader:
    def __init__(self,code:str,testcases:list[str],section:int,timeout:float) -> None:
        self.code = code
        self.testcases = testcases
        self.section = section
        self.timeout = timeout

    def import_testcases(self) -> None:
        for i in range(len(self.testcases)):
            with open(f'./api/sandbox/section{self.section}/testcases/{i}.txt','w') as f:
                f.write(self.testcases[i])

    def import_source_code(self) -> None:
        pass

    def setup(self) -> None:
        self.import_testcases()
        self.import_source_code()
        
    def compile(self) -> None:
        pass

    def runtime(self) -> list[RuntimeResult]:
        pass
        
    def generate_output(self) -> list[RuntimeResult]:
        self.setup()
        self.compile()
        return self.runtime()

    def grading(self,expected_output:list[str]) -> list[dict]:
        self.setup()
        self.compile()
        runtime_result = self.runtime()

        if len(runtime_result) != len(expected_output):
            raise Exception("Length of expected output and runtime result is not equal")
        
        grading_result = []
        for i in range(len(runtime_result)):

            is_passed = False
            output = None

            if runtime_result[i].runtime_status == "OK":
                
                output = runtime_result[i].output
                if forgiveableFormat(runtime_result[i].output) == forgiveableFormat(expected_output[i]):
                    is_passed = True
            
            grading_result.append({
                "input": runtime_result[i].input,
                "output": output,
                "runtime_status": runtime_result[i].runtime_status,
                "expected_output": expected_output[i],
                "is_passed": is_passed
            })

        return grading_result

class PythonGrader(ProgramGrader):

    def import_source_code(self) -> None:
        with open(f'./api/sandbox/section{self.section}/runner.py','w') as f:
            f.write(self.code)

    def runtime(self) -> list[RuntimeResult]:
        
        result = []
        
        for i in range(len(self.testcases)):
            try:
                runner = subprocess.check_output([
                    'python',f'./api/sandbox/section{self.section}/runner.py'],
                    stdin=open(f'./api/sandbox/section{self.section}/testcases/{i}.txt',
                    'r'
                ),stderr=subprocess.DEVNULL,timeout=float(self.timeout))
                result.append(RuntimeResult(self.testcases[i],runner.decode(),"OK"))
            except subprocess.CalledProcessError:
                result.append(RuntimeResult(self.testcases[i],None,"ERROR"))
            except subprocess.TimeoutExpired:
                result.append(RuntimeResult(self.testcases[i],None,"TIMEOUT"))

        return result

class CGrader(ProgramGrader):

    def import_source_code(self) -> None:
        with open(f'./api/sandbox/section{self.section}/runner.c','w') as f:
            f.write(self.code)

    def compile(self) -> None:
        subprocess.check_output(['gcc',f'./api/sandbox/section{self.section}/runner.c','-o',f'./api/sandbox/section{self.section}/runner.exe'],stderr=subprocess.DEVNULL)

    def runtime(self) -> list[RuntimeResult]:
            
            result = []
            
            for i in range(len(self.testcases)):
                try:
                    runner = subprocess.check_output([
                        f'./api/sandbox/section{self.section}/runner.exe'],
                        stdin=open(f'./api/sandbox/section{self.section}/testcases/{i}.txt',
                        'r'
                    ),stderr=subprocess.DEVNULL,timeout=float(self.timeout))
                    result.append(RuntimeResult(self.testcases[i],runner.decode(),"OK"))
                except subprocess.CalledProcessError:
                    result.append(RuntimeResult(self.testcases[i],None,"ERROR"))
                except subprocess.TimeoutExpired:
                    result.append(RuntimeResult(self.testcases[i],None,"TIMEOUT"))
    
            return result

class CppGrader(ProgramGrader):
    def import_source_code(self) -> None:
        with open(f'./api/sandbox/section{self.section}/runner.cpp','w') as f:
            f.write(self.code)

    def compile(self) -> None:
        subprocess.check_output(['g++',f'./api/sandbox/section{self.section}/runner.cpp','-o',f'./api/sandbox/section{self.section}/runner.exe'],stderr=subprocess.DEVNULL)

    def runtime(self) -> list[RuntimeResult]:
            
            result = []
            
            for i in range(len(self.testcases)):
                try:
                    runner = subprocess.check_output([
                        f'./api/sandbox/section{self.section}/runner.exe'],
                        stdin=open(f'./api/sandbox/section{self.section}/testcases/{i}.txt',
                        'r'
                    ),stderr=subprocess.DEVNULL,timeout=float(self.timeout))
                    result.append(RuntimeResult(self.testcases[i],runner.decode(),"OK"))
                except subprocess.CalledProcessError:
                    result.append(RuntimeResult(self.testcases[i],None,"ERROR"))
                except subprocess.TimeoutExpired:
                    result.append(RuntimeResult(self.testcases[i],None,"TIMEOUT"))
    
            return result


adder = '''
x = int(input("x: "))
y = int(input("y: "))
while True:
    pass
'''

adderC = r'''
#include <stdio.h>

int main() {
    int a,b;
    scanf("%d",&a);
    scanf("%d",&b);
    printf("%d\n",a-b);
    return 0;
}
'''

adderCpp = r'''
#include <iostream>
using namespace std;

int main() {
    int a,b;
    cin >> a;
    cin >> b;

    cout << a - b << "\n";    
}
'''

test = [
'''1
2
''',
'''52
18
''',
'''9
-5
'''
]

pyresult = ["x: y: -1\r\n","x: y: 34\r\n","x: y: 14\r\n"]
cresult = ["-1\r\n","34\r\n","14\r\n"]

program1 = CppGrader(adderCpp,test,1,1.5)
for i in program1.grading(cresult):
    print(i)