import React from 'react';
import { Link, useHistory } from 'react-router-dom';
import styled from 'styled-components';

import { logoutRequest } from 'apis/authApi';

const StyledHeader = styled.header`
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-sizing: border-box;
    width: 100%;
    height: 80px;
    padding: 0 50px;
    background-color: #4B6587;
    font-size: 1.1rem;
    color: #EEEEEE;

    > h1 {
        font-size: 1.5rem;
        font-weight: bold;
    }

    ul {
        display: flex;
    }

    li {
        cursor: pointer;
        transition: all 100ms ease-in-out 0ms;
    }

    li:hover {
        transform: scale(1.1);
    }

    li + li {
        margin-left: 20px;
    }

    a {
        text-decoration: none;
        color: #EEEEEE;
    }
`

const Header = ({ loginId, setLoginId }) => {
    const history = useHistory();

    const handleLogoutButton = async () => {
        try {
            if (window.confirm("정말로 로그아웃 하시겠습니까?")) {
                await logoutRequest();
                window.sessionStorage.clear();
                setLoginId(null);
                alert("로그아웃 되었습니다.");
                history.push("/login");
            }
        }
        catch (e) {
            if (e.response.status === 401) {
                alert("로그아웃 되었습니다.");
                window.sessionStorage.clear();
                setLoginId(null);
                history.push("/login");
            }
        }
    }

    return (
        <StyledHeader>
            <h1>RacerIn</h1>
            {
                loginId && (
                    <nav>
                        <ul>
                            <li><Link to="/">메인</Link></li>
                            <li><Link to="/search">네트워크</Link></li>
                            <li onClick={() => { handleLogoutButton() }}>로그아웃</li>
                        </ul>
                    </nav>
                )
            }
        </StyledHeader>
    )
}

export default Header