import React, { useEffect,useState } from 'react'; //리액트 불러오기
import console from 'react-console'; //리액트 콘솔_크롬으로 실행
import './test.css?v=1.0';//test.css 불러오기

const Test = ( { history } ) =>
 {
	const questions = [
		{
			questionText: '머리카락이 어떤 색에 가깝나요?',
			answerOptions: [
				{ answerText: '검은색', isCorrect: true },
				{ answerText: '갈색', isCorrect: false }
			],
		},
		{
			questionText: '피부에 붉은 기가 많다',
			answerOptions: [
				{ answerText: '예', isCorrect: true },
				{ answerText: '아니오', isCorrect: false }
			],
		},
		{
			questionText: '손목 혈관 색이 파란색보다는 초록색이다',
			answerOptions: [
				{ answerText: '예', isCorrect: false },
				{ answerText: '아니오', isCorrect: true }
			],
		},
		{
			questionText: '햇볕에 장시간 있으면 피부가...',
			answerOptions: [
				{ answerText: '붉어진다', isCorrect: true },
				{ answerText: '검게 그을린다', isCorrect: false }
			],
		},
		{
			questionText: '순백 셔츠보다 아이보리색이 더 어울리나요?',
			answerOptions: [
				{ answerText: '예', isCorrect: false },
				{ answerText: '아니오', isCorrect: true }
			],
		},
		{
			questionText: '나는 OO색의 악세사리가 어울린다',
			answerOptions: [
				{ answerText: '골드', isCorrect: false },
				{ answerText: '실버', isCorrect: true }
			],
		},
		{
			questionText: '눈동자가 어떤 색에 가깝나요?',
			answerOptions: [
				{ answerText: '갈색', isCorrect: false },
				{ answerText: '검은색', isCorrect: true }
			],
		},
		{
			questionText: '맨 얼굴로 검은색 옷을 입으면...',
			answerOptions: [
				{ answerText: '칙칙해보인다', isCorrect: false },
				{ answerText: '이목구비가 뚜렷해보인다', isCorrect: true }
			],
		},
		{
			questionText: '얼굴이 창백해보인다는 소리를 자주 듣나요?',
			answerOptions: [
				{ answerText: '예', isCorrect: true },
				{ answerText: '아니오', isCorrect: false }
			],
		},
		{
			questionText: '손가락을 지그시 눌러 피가 몰려있을 때...',
			answerOptions: [
				{ answerText: '탁한 빨간색이다', isCorrect: false },
				{ answerText: '분홍색이다', isCorrect: true }
			],
		},
		{
			questionText: '주변에서 나의 첫 인상은...',
			answerOptions: [
				{ answerText: '차가운 분위기가 난다', isCorrect: true },
				{ answerText: '따뜻한 분위기가 난다', isCorrect: false }
			],
		},
	]; //웜,쿨 파악

	const [currentQuestion, setCurrentQuestion] = useState(0); //현재 문제 번호 [변수, 함수]
	const [showScore, setShowScore] = useState(false); //결과 보여줄까?
    const [score_c, setScore_cool] = useState(0); //쿨톤 점수 -> 웜,쿨 리스트에서 사용
	const [score_w, setScore_warm] = useState(0); //웜톤 점수 -> 웜,쿨 리스트에서 사용
	const [score, setPersonal] = useState(""); //퍼스널컬러 결과
	const [num, setNum] = useState(0);

	const handleAnswerOptionClick = (isCorrect) => {  //main 함수 1_웜쿨 검사
		if (isCorrect) {
			setScore_cool(score_c + 1);
			console.log('c' + score_c);
		}
		else{
			setScore_warm(score_w + 1);
			console.log('w' + score_w);
		} ///웜,쿨 if문으로 점수 올리기

		const nextQuestion = currentQuestion + 1;
		if (nextQuestion < questions.length) {
			setCurrentQuestion(nextQuestion);
		}
		else{
			setShowScore(true); //questions 끝나면 점수 보여줄까? true -> className='score-section'
		}
       
 }; //함수1 끝.

 const handlePersonalScore = (score_c,score_w) =>{ //함수2_웜,쿨 점수로 결과 구하기
	if(score_c>score_w){
		setPersonal('cool');
	}
	else if(score_c<score_w){
		setPersonal('warm');
	}
	else{
		setPersonal('restart');
	}
	setNum(num + 1);
}; //함수2 끝.

	return (
		<div id='test'>
			<head>
				<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.7.2/animate.min.css"></link>
			</head>
			{showScore ? ( 
				<span className='score-section'>
					<button  className="animated infinite pulse" id="result" onClick={() => handlePersonalScore(score_c,score_w)}>result</button>
					{num === 1 ?
					(<div className = "season">
						{score === "cool" ? (<button id='next' onClick={ () => {history.push("/test2")}}>next</button>)
						: (<button id='next' onClick={ () => {history.push("/test3")}}>next</button>)}
					</div>)
						: (<div>click result!</div>)}
				</span>
			) : (
				<>
				<div className='question-section'>
					<div id='question-count'>
						<span>Question {currentQuestion + 1}</span>/{questions.length}
						<div className="animated infinite pulse">{questions[currentQuestion].questionText}</div>
					</div>
				</div>
				<div className='answer-section'>
					{questions[currentQuestion].answerOptions.map((answerOption) => (
						<button id = "btn_answer" onClick={() => handleAnswerOptionClick(answerOption.isCorrect)}>{answerOption.answerText}</button>
					))}
				</div>
				</>
			)}
		</div>
	);
}


export default Test;