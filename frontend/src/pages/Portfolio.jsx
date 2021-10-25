import React, { useState, useEffect } from "react";
import { useHistory, useParams, Redirect } from "react-router-dom";
import styled from "styled-components";

import { fetchPortfolio } from "apis/portfolioApi";
import Message from "components/Message";
import ProfileCard from "components/ProfileCard";
import AwardCard from "components/portfolio/AwardCard"
import EducationCard from "components/portfolio/EducationCard";
import LicenseCard from "components/portfolio/LicenseCard";
import ProjectCard from "components/portfolio/ProjectCard";

const PortfolioWrapper = styled.div`
    margin: 10px;
    width: 100%;
`

const PortfolioMain = styled.main`
    display: flex;
    align-items: flex-start;
    min-height: calc(100vh - 80px);
    box-sizing: border-box;
    margin: 0 auto;
    padding: 80px 0;
    max-width: 960px;
    width: 100%;
    color: #EEEEEE;
`

const Portfolio = ({ loginId, setLoginId }) => {
    const [portfolio, setPortfolio] = useState(null);
    const { id: currentUser } = useParams();
    const history = useHistory();

    useEffect(() => {
        const userId = currentUser ? currentUser : loginId;
        if (loginId === null) return;
        (async () => {
            try {
                const data = await fetchPortfolio(userId);
                setPortfolio(data);
            } catch (e) {
                if (e.response.status === 401) {
                    alert("세션이 만료되었습니다.");
                    window.sessionStorage.clear();
                    setLoginId(null);
                    history.push("/login");
                }
                if (e.response.status === 404) {
                    history.push("/page404");
                }
            }
        })();
    }, [currentUser, loginId, history, setLoginId]);

    return (
        <PortfolioMain>
            {loginId === null && <Redirect to="/login" />}
            {
                portfolio === null
                    ? <Message><h2>로딩 중</h2></Message>
                    : (
                        <>
                            <ProfileCard
                                user={portfolio.user}
                                setLoginId={setLoginId}
                                isEditAble={currentUser === undefined || Number(currentUser) === Number(loginId)}
                                setPortfolio={setPortfolio}
                            />
                            <PortfolioWrapper>
                                <EducationCard
                                    educations={portfolio.educations}
                                    loginId={loginId}
                                    setLoginId={setLoginId}
                                    isEditAble={currentUser === undefined || Number(currentUser) === Number(loginId)}
                                    setPortfolio={setPortfolio}
                                />
                                <AwardCard
                                    awards={portfolio.awards}
                                    loginId={loginId}
                                    setLoginId={setLoginId}
                                    isEditAble={currentUser === undefined || Number(currentUser) === Number(loginId)}
                                    setPortfolio={setPortfolio}
                                />
                                <ProjectCard
                                    projects={portfolio.projects}
                                    loginId={loginId}
                                    setLoginId={setLoginId}
                                    isEditAble={currentUser === undefined || Number(currentUser) === Number(loginId)}
                                    setPortfolio={setPortfolio}
                                />
                                <LicenseCard
                                    licenses={portfolio.licenses}
                                    loginId={loginId}
                                    setLoginId={setLoginId}
                                    isEditAble={currentUser === undefined || Number(currentUser) === Number(loginId)}
                                    setPortfolio={setPortfolio}
                                />
                            </PortfolioWrapper>
                        </>
                    )
            }
        </PortfolioMain>
    )
};

export default Portfolio;