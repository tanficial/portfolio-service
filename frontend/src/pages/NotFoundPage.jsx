import { Redirect, useHistory } from "react-router";
import styled from "styled-components";

import Message from "components/Message";

const Button = styled.button`
    border: none;
    box-sizing: border-box;
    background-color: #4B6587;
    cursor: pointer;
    font-size: 14px;
    font-weight: bold;
    padding: 6px 12px;
    color: white;

    :hover {
        transform: scale(1.1);
    }
`
const NotFoundPage = ({ loginId }) => {
    const history = useHistory();
    return (
        <Message>
            {loginId === null && <Redirect to="/login" />}
            <h2>존재하지 않는 페이지 입니다.</h2>
            <Button onClick={() => history.push("/")}>메인 화면으로 돌아가기</Button>
        </Message>
    )
}

export default NotFoundPage;